import boto3
import logging
from botocore.exceptions import ClientError

client = boto3.client("s3")
# bucket without location 
def create_bucket_without_location(bucket_name):
    try:
        client.create_bucket(Bucket = bucket_name)
        print("Bucket created successfully")
    except ClientError as e:
        logging.error(e)
        print("An error occurred. it can either be the internet connection or credentials no configured correctly")

# bucket with location
def create_bucket_with_location(bucket_name, bucket_region):
    try:
        client = boto3.client('s3', region_name=bucket_region)
        location = {'LocationConstraint': bucket_region}
        client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)
        print("bucket has been created successfully")
    except ClientError as e:
        logging.error(e)
        print("Error!, it can either be the internet connection or credentials no configured correctly")

def display_existing_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


while True:
    question_if_want_to_create_bucket = input(" Please do you want to create bucket (Y/N): ").upper()
    if question_if_want_to_create_bucket == "Y":
        name_of_bucket = input("Please enter a unique bucket name: ")
        question_if_want_to_create_region_and_specific_region = input(" Please do you want to create the bucket in a specific region? (Y/N): ").upper()
        if question_if_want_to_create_region_and_specific_region == "Y":
            specify_region = input("Please enter the region you want the bucket to be created, and should be in a format similer to this (af-south-1): ")
            print( create_bucket_with_location (name_of_bucket,specify_region ))
        else :
            print(create_bucket_without_location(name_of_bucket))
    else:
        display_existing_s3_buckets()
        print("Bye Bye")

    break



