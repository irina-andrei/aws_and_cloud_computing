import boto3

s3 = boto3.client('s3')
# this stores the connection to aws

s3.Bucket('tech254-irina-bucket-test').download_file('example.txt', 's3_downloads')
# downloading file
# s3.Bucket('BUCKET_NAME').download_file('OBJECT_NAME', 'FILE_NAME')

print("Download was successful.")
# printing back an output message to show the download was successful.
