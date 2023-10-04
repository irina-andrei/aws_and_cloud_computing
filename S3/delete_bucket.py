import boto3

s3 = boto3.client('s3')
# this stores the connection to aws

s3.delete_bucket(Bucket='tech254-irina-bucket-test')
# deleting bucket
# s3.delete_bucket(Bucket=bucket_name)

print("Deletion was successful.")
# printing back an output message to show the deletion was successful.
