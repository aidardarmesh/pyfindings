import boto3

def delete_s3_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    try:
        # Delete all objects in the bucket
        bucket.objects.all().delete()
        print(f"All objects in bucket {bucket_name} have been deleted.")

        # Delete the bucket
        bucket.delete()
        print(f"Bucket {bucket_name} has been deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")

if __name__ == '__main__':
    bucket_name = 'elasticbeanstalk-eu-central-1-992382639776'
    delete_s3_bucket(bucket_name)
