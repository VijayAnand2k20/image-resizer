# ImageOptimizer API

The ImageOptimizer API is a serverless solution for automatically resizing images using AWS Lambda and Amazon S3. This documentation provides details on how to set up, deploy, and use the API.

## Getting Started

### Prerequisites

- AWS Account: You need an AWS account to deploy the Lambda function and API Gateway.
- Postman: For testing API requests.

### Deployment

1. **Deploy the Lambda Function:**
   - Create an S3 bucket for image storage.
   - Create an IAM role with necessary permissions for Lambda to access S3.
   - Deploy the Lambda function using the provided code.

2. **Set Up API Gateway:**
   - Create a new API in API Gateway.
   - Create a resource and method to trigger the Lambda function.
   - Deploy the API to obtain the endpoint URL.

## Usage

Use Postman or any HTTP client to send POST requests to the API endpoint. The payload should resemble the following:

```json
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "your-s3-bucket-name"
        },
        "object": {
          "key": "path/to/your/image.jpg"
        }
      }
    }
  ]
}
```

## Monitoring (Continued)

### CloudWatch Logs

For detailed insights into the execution of your Lambda function, you can check the CloudWatch Logs. Follow these steps:

1. Open the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
2. Navigate to your Lambda function (`ImageOptimizer`).
3. Click on the "Monitoring" tab.
4. Scroll down to the "Log groups" section and click on the associated CloudWatch Log Group link.

### API Gateway Metrics

Monitor API Gateway for request and error metrics. Follow these steps:

1. Open the [API Gateway console](https://console.aws.amazon.com/apigateway/).
2. Navigate to your API.
3. In the API Gateway dashboard, explore the available metrics.

## Troubleshooting

If you encounter issues, consider the following steps:

1. **IAM Roles and Permissions:**
   - Ensure that the IAM role associated with your Lambda function has the necessary permissions to read from and write to the S3 bucket.

2. **CloudWatch Logs:**
   - Check CloudWatch Logs for your Lambda function to identify any error messages or unexpected behavior.

3. **API Gateway Settings:**
   - Review API Gateway settings and logs for any issues related to request handling or Lambda function integration.

## Contributing

Contributions are welcome! If you have suggestions, find a bug, or want to contribute to the project, feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

