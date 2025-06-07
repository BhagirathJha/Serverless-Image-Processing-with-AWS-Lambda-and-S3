resource "aws_lambda_function" "resize_image" {
  filename         = "resize_image.zip"
  function_name    = "resize_image"
  role             = aws_iam_role.lambda_role.arn
  handler          = "resize_image.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = filebase64sha256("resize_image.zip")
  timeout          = 30
}
