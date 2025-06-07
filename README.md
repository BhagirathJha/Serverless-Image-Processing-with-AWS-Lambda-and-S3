
# Image Resizer with AWS Lambda & S3 Buckets

This project is an automated image resizing using AWS services. It utilizes **S3 Buckets**, **AWS Lambda**, and **Terraform (HCL)** for infrastructure as code. The architecture is designed to automatically resize uploaded images and store the resized versions separately.

---

## 🛠️ Tools & Technologies

- **AWS** – Cloud platform used for S3 and Lambda
- **Terraform** – Infrastructure as Code (IaC) tool for provisioning AWS resources
- **Visual Studio Code (VSCode)** – Code editor
- **Git** – Version control system

---

## Dependency

Dependency of python package for resize_image.py file is [pillow](https://pypi.org/project/pillow/) you need to install.

```bash
pip install pillow
```

## 📐 Architecture Overview

1. **Two S3 Buckets**:
   - **Source Bucket** – Where users upload original images.
   - **Destination Bucket** – Stores resized images after processing.

2. **Lambda Function**:
   - Automatically triggered via **S3 Event Notification** when a new image is uploaded to the source bucket.
   - Processes the image and resizes it.
   - Uploads the resized image to the destination bucket.

3. **Event Flow**:
   - User uploads an image to the **Source Bucket**.
   - S3 triggers an event that invokes the **Lambda Function**.
   - Lambda resizes the image (making it smaller than the original).
   - Resized image is saved to the **Destination Bucket**.

---

## 🧾 Language

- **HCL (HashiCorp Configuration Language)** – used for defining AWS infrastructure with Terraform.

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BhagirathJha/Serverless-Image-Processing-with-AWS-Lambda-and-S3.git
   cd Serverless-Image-Processing-with-AWS-Lambda-and-S3
   ```


## Infrastructure

<p align="center">
  <img src="https://github.com/BhagirathJha/Serverless-Image-Processing-with-AWS-Lambda-and-S3/blob/main/S3_Lambda.png" height="210" width="1360">
</p>

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Bhagirath Jha](https://github.com/BhagirathJha)
