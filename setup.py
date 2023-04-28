from setuptools import setup, find_packages
from codecs import open
from os import path

path.abspath(path.dirname(__file__))

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

packages = find_packages()

setup(
    name='cfn2sam',
    version='0.1.0',
    description='An open-source tool for converting CloudFormation templates to SAM templates',
    long_description=long_description,
    author='Rahul Lokurte',
    author_email='rahul.m.lokurte@gmail.com',
    url='https://github.com/rahulmlokurte/CloudFormation2SAM',
    packages=packages,
    entry_points={
        'console_scripts': [
            'cfn2sam = cfn2sam.cli:main',
        ],
    },
    install_requires=[
        'PyYAML==6.0', 'boto3==1.26.120', 'PyYAML==6.0'
    ],
)
