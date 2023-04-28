import argparse

from cfn2sam.conversion import convert_to_sam


def main():
    """Entrypoint for cfn2sam when invoked as a module with python -m cfn2sam"""
    parser = argparse.ArgumentParser(description='Convert a CloudFormation template to a SAM template.')
    parser.add_argument('--cloud_formation_file', required=True, type=argparse.FileType('r'),
                        help='path to the input CloudFormation template file')
    parser.add_argument('--aws_sam_file',  required=True, type=argparse.FileType('w'),
                        help='path to the output SAM template file')
    args = parser.parse_args()

    # call the function convert_to_sam from conversion.py
    convert_to_sam(args.cloud_formation_file, args.aws_sam_file)

