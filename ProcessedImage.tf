resource "aws_s3_bucket" "ProcesstheImages" {
    bucket = "processtheimages"
    
    tags = {
        Name = "processtheimages"
    }
  
}