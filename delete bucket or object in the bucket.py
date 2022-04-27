import logging

import boto3
from botocore.exceptions import ClientError

client = boto3.client("s3")

#display existing bucket
def display_Existing_bucket():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def delete_bucket(bucket_name_to_be_deleted):
    bucket_name_to_be_deleted = input(" Please enter the name of bucket to be deleted: ")
    try:
        client.delete_bucket(Bucket=bucket_name_to_be_deleted)
        print("bucket deleted successfully")
    except ClientError as e:
        logging.error(e)
        print("Error!, this could be either invalid bucket name or network connection")
def list_bucket_object():
    bucket_name = input("Please enter a bucket name: ")
    s3 = boto3.resource("s3")
    list_re = s3.Bucket(bucket_name)
    for object in list_re.objects.all():
        print(object.key)

def delete_object_in_bucket():
    try:
        bucket_name = input("Please enter a bucket that you want to delete an object in it: ")
        s3 = boto3.resource("s3")
        list_re = s3.Bucket(bucket_name)
        for object in list_re.objects.all():
             print(object.key)
        try:
            file_name = input("please enter the file name you want to delete ")
            client = boto3.client("s3")
            client.delete_object(Bucket=bucket_name, Key=file_name)
        except ClientError as e:
            logging.error(e)
            print("Error!, object not in bucket or network connection problem")

    except ClientError as e:
        logging.error(e)
        print("Error!, bucket not available or network connection")

while True:
    ask_what_do_you_want = input("what action do you want to perform?. do you wat to see existing bucket(EB), list the object in bucket(LOB), delete bucket(DB) or delete object in bucket(DOB)?: ").upper()
    if ask_what_do_you_want == "EB":
        print(display_Existing_bucket())
    elif ask_what_do_you_want == "LOB":
            print(display_Existing_bucket())
            print(list_bucket_object())
    elif ask_what_do_you_want == "DB":
        print(display_Existing_bucket())
        bucket_name = input(" Are you sure you want to delete a bucket(Y/N)?: ").upper()
        if bucket_name == "Y":
           print(delete_bucket(bucket_name_to_be_deleted=bucket_name))
        else:
            print("bye bye!")
    elif ask_what_do_you_want == "DOB":
        print(display_Existing_bucket())
        print(delete_object_in_bucket())
    else:
        print("bye bye!")
    break



