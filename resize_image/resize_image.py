import boto3
from PIL import Image, UnidentifiedImageError
from io import BytesIO

s3 = boto3.client('s3')

SUPPORTED_FORMATS = {'JPEG', 'PNG', 'GIF', 'WEBP', 'BMP', 'TIFF'}

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            destination_bucket = 'processtheimages'

            # Download the image
            response = s3.get_object(Bucket=source_bucket, Key=key)
            image_content = response['Body'].read()

            # Open and resize image
            try:
                img = Image.open(BytesIO(image_content))
            except UnidentifiedImageError:
                return {
                    'statusCode': 400,
                    'body': f'Unsupported or corrupted image: {key}'
                }

            img.thumbnail((100, 100))  # Resize to thumbnail

            # Determine safe format
            img_format = img.format.upper() if img.format else 'JPEG'
            if img_format not in SUPPORTED_FORMATS:
                img_format = 'JPEG'

            # Convert image mode if required (e.g., RGBA to RGB for JPEG)
            if img_format == 'JPEG' and img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')

            # Save resized image to buffer
            buffer = BytesIO()
            img.save(buffer, format=img_format)
            buffer.seek(0)

            # Upload to destination bucket
            s3.put_object(
                Bucket=destination_bucket,
                Key=key,
                Body=buffer,
                ContentType=response.get('ContentType', f'image/{img_format.lower()}')
            )

        return {
            'statusCode': 200,
            'body': 'Image(s) resized and uploaded successfully.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error processing image: {str(e)}'
        }
