resource "aws_s3_bucket" "StoretheImage" {
    bucket = "storetheimage"
    
    tags = {
        Name = "storetheimage"
    }
  
}
