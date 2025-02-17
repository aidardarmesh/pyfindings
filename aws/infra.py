import boto3

AWS_REGIONS = [
    'us-east-1',      # N. Virginia
    'us-east-2',      # Ohio
    'us-west-1',      # N. California
    'us-west-2',      # Oregon
    'af-south-1',     # Cape Town
    'ap-east-1',      # Hong Kong
    'ap-south-1',     # Mumbai
    'ap-northeast-3', # Osaka
    'ap-northeast-2', # Seoul
    'ap-southeast-1', # Singapore
    'ap-southeast-2', # Sydney
    'ap-northeast-1', # Tokyo
    'ca-central-1',   # Canada Central
    'eu-central-1',   # Frankfurt
    'eu-west-1',      # Ireland
    'eu-west-2',      # London
    'eu-south-1',     # Milan
    'eu-west-3',      # Paris
    'eu-north-1',     # Stockholm
    'me-south-1',     # Bahrain
    'sa-east-1'       # São Paulo
]

def delete_vpcs(region_name: str) -> None:
    ec2 = boto3.client('ec2', region_name=region_name)
    try:
        vpcs = ec2.describe_vpcs()
        vpc_ids = [vpc['VpcId'] for vpc in vpcs['Vpcs']]
        if vpc_ids:
            for vpc_id in vpc_ids:
                # Delete dependencies
                delete_dependencies(ec2, vpc_id)
                ec2.delete_vpc(VpcId=vpc_id)
            print(f"Deleted VPCs in {region_name}: {vpc_ids}")
        else:
            print(f"No VPCs found in {region_name}")
    except Exception as e:
        print(f"Error retrieving or deleting VPCs from {region_name}: {e}")

def delete_dependencies(ec2, vpc_id: str) -> None:
    # Delete subnets
    subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    subnet_ids = [subnet['SubnetId'] for subnet in subnets['Subnets']]
    for subnet_id in subnet_ids:
        ec2.delete_subnet(SubnetId=subnet_id)

    # Delete security groups
    security_groups = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    security_group_ids = [sg['GroupId'] for sg in security_groups['SecurityGroups']]
    for sg_id in security_group_ids:
        ec2.delete_security_group(GroupId=sg_id)

    # Delete route tables
    route_tables = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    route_table_ids = [rt['RouteTableId'] for rt in route_tables['RouteTables']]
    for rt_id in route_table_ids:
        ec2.delete_route_table(RouteTableId=rt_id)

    # Delete internet gateways
    igws = ec2.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])
    igw_ids = [igw['InternetGatewayId'] for igw in igws['InternetGateways']]
    for igw_id in igw_ids:
        ec2.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        ec2.delete_internet_gateway(InternetGatewayId=igw_id)

if __name__ == '__main__':
    for region_name in AWS_REGIONS:
        delete_vpcs(region_name=region_name)
