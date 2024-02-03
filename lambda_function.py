import os
import boto3
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket and key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the image from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    image_content = response['Body'].read()

    # Resize the image
    resized_image = resize_image(image_content)

    # Upload the resized image back to S3
    resized_key = f"resized/{os.path.basename(key)}"
    s3.put_object(Body=resized_image, Bucket=bucket, Key=resized_key)

    print(f"Resized image uploaded to: {resized_key}")

def resize_image(image_content):
    # Open the image using PIL
    image = Image.open(BytesIO(image_content))

    # Resize the image to a fixed width of 300 pixels
    width = 300
    height = int((width / float(image.size[0])) * float(image.size[1]))
    resized_image = image.resize((width, height))

    # Save the resized image to a BytesIO object
    resized_image_io = BytesIO()
    resized_image.save(resized_image_io, format='JPEG')
    resized_image_io.seek(0)

    return resized_image_io.read()
