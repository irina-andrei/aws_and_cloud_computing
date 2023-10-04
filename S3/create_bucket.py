import boto3

s3 = boto3.client('s3')
# this stores the connection to aws

s3.create_bucket(Bucket='tech254-irina-bucket-test',
                CreateBucketConfiguration={
                        'LocationConstraint': 'eu-west-1'
                                        })
# creating the bucket

print("Creation of bucket was successful.")
# printing back an output message to show the creation was successful.