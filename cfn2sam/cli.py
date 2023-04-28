import argparse

from cfn2sam.validation.cloud_formation_validation import is_cloud_formation_template_valid


def main():
    """Entrypoint for cfn2sam when invoked as a module with python -m cfn2sam"""
    parser = argparse.ArgumentParser(description='Convert a CloudFormation template to a SAM template.')
    parser.add_argument('--cfn-file', dest='cloud_formation_file', required=True,
                        help='path to the input CloudFormation template file')
    parser.add_argument('--sam-file', dest='aws_sam_file', nargs='?',
                        help='path to the output SAM template file')

    subparsers = parser.add_subparsers(title='subcommands')

    validate_parser = subparsers.add_parser('validate', help='validate a CloudFormation template')
    validate_parser.set_defaults(func=is_cloud_formation_template_valid())

    args = parser.parse_args()
    print(args.aws_sam_file)
    print(type(args.aws_sam_file))
    args.func(args)
