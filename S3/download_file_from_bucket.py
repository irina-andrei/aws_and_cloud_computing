import boto3

s3 = boto3.client('s3')
# this stores the connection to aws

s3.download_file('tech254-irina-bucket-test', 'example.txt', 'new_example.txt')
# downloading file
# s3.download_file('BUCKET_NAME', 'FILE_IN_BUCKET', 'NEW_FILE_NAME')

print("Download was successful.")
# printing back an output message to show the download was successful.
