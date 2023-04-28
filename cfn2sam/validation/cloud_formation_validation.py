import boto3


def is_cloud_formation_template_valid(template_body):
    cfn_client = boto3.client('cloudformation')
    try:
        cfn_client.validate_template(TemplateBody=template_body)
        return True
    except Exception as e:
        print(f'Error validating CloudFormation template: {e}')
        return False
