#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import AwsProvider, Instance
from imports.terraform_aws_modules.vpc.aws import TerraformAwsModulesVpcAws
from imports.terraform_aws_modules.security_group.aws import TerraformAwsModulesSecurityGroupAws
from imports.terraform_aws_modules.s3_bucket.aws import TerraformAwsModulesS3BucketAws


user_data = """#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 8080 &
"""

class MyStack(TerraformStack):

    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, 'Aws', region='eu-central-1')

        # bucketname = 'cdktest-wiwa'
        # TerraformAwsModulesS3BucketAws(self, 'bucket', bucket = bucketname)

        my_vpc =  TerraformAwsModulesVpcAws(self, 
            id='vpc',
            name ="test-vpc",
            cidr = "10.0.0.0/16",
            azs = ["eu-central-1a"],
            public_subnets = ["10.0.101.0/24"]   
        )

        newInstance = Instance(self, 'pythondemo',
            ami="ami-0a02ee601d742e89f",
            instance_type="t2.micro",
            availability_zone="eu-central-1a",
            associate_public_ip_address=True,
            tags={"Name": "Python-Demo-updated"},
            user_data = user_data,
            subnet_id =my_vpc.public_subnets_output
        )

        TerraformOutput(self, 'pythondemo_public_ip',
            value=newInstance.public_ip
        )

app = App()
MyStack(app, "TerraformCDK")

app.synth()
