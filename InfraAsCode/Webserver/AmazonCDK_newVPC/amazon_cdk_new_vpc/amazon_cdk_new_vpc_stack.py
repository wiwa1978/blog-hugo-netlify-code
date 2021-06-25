from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (core, aws_ec2 as ec2)

instanceName="aws-cdk-instance"
instanceType="t2.micro"
amiName="amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2" 

script = """#!/bin/bash
echo "Hello, World! Updated version" > index.html
nohup python -m SimpleHTTPServer 8080 &
"""

user_data = ec2.UserData.custom(script)

class AmazonCdkNewVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "vpc",
            cidr = "10.24.0.0/16",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=20, subnet_type=ec2.SubnetType.PUBLIC ),
                ec2.SubnetConfiguration(name="private", cidr_mask=20, subnet_type=ec2.SubnetType.PRIVATE )
            ]
        )
   
        core.Tag.add(scope=vpc, key='Name', value='newCDKVPC')
     


        # create a new security group
        sec_group = ec2.SecurityGroup(
            self,
            "sec-group-allow-http",
            vpc=vpc,
            allow_all_outbound=True
        )

        # add a new ingress rule to allow port 8080 to internal hosts
        sec_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/0'),
            description="Allow HTTP connection", 
            connection=ec2.Port.tcp(8080)
        )

        # define a new ec2 instance
        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name=instanceName,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            vpc=vpc,
            availability_zone="eu-central-1b",
            security_group=sec_group,
            user_data=user_data
        )


