import boto3, pprint

# Create a SageMaker client
sagemaker_client = boto3.client("sagemaker")

# List all SageMaker domains
response = sagemaker_client.list_domains()

# Extract and print the DomainId(s)
for domain in response["Domains"]:
    pprint.pprint(domain)
    print(f"Domain ID: {domain['DomainId']}")
