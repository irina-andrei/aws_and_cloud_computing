import boto3

s3 = boto3.client('s3')
# this stores the connection to aws

s3.upload_file('/home/ubuntu', 'tech254-irina-bucket-test', 'example.txt')
# uploading file
# s3.upload_file('/path/to/local/file', 'bucket-name', 'your-object-name')

print("Upload was successful.")
# printing back an output message to show the upload was successful.