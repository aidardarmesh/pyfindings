import boto3

def get_current_user_details():
    iam = boto3.client('iam')

    try:
        user = iam.get_user()
        return user['User']
    except Exception as e:
        print(f"Error retrieving user details: {e}")
        return None

def attach_policy_to_current_user(policy_arn):
    iam = boto3.client('iam')
    user = get_current_user_details()

    if user:
        try:
            iam.attach_user_policy(UserName=user['UserName'], PolicyArn=policy_arn)
            print(f"Policy {policy_arn} has been attached to user {user['UserName']} successfully.")
        except Exception as e:
            print(f"Error attaching policy {policy_arn} to user {user['UserName']}: {e}")


if __name__ == '__main__':
    # get_current_user_details()
    attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DescribeSecurityGroups')
    # attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DescribeSubnets')
    # attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DescribeVpcs')
    # attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DeleteSecurityGroup')
    # attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DeleteSubnet')
    # attach_policy_to_current_user('arn:aws:iam::aws:policy/ec2:DeleteVpc')
