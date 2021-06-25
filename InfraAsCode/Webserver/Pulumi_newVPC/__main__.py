import pulumi
import pulumi_aws as aws

size = 't3.micro'

user_data = """#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 8080 &
"""

ami = aws.ec2.get_ami(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])

my_vpc = aws.ec2.Vpc("myVpc",
    cidr_block="172.16.0.0/16",
    tags={
        "Name": "pulumi-new-vpc",
    })

my_subnet = aws.ec2.Subnet("mySubnet",
    vpc_id=my_vpc.id,
    cidr_block="172.16.10.0/24",
    availability_zone="eu-central-1a",
    map_public_ip_on_launch=True,
    tags={
        "Name": "pulumi-new-subnet",
    })

group = aws.ec2.SecurityGroup('pulumi_allow_8080',
            vpc_id=my_vpc.id,
            description='Enable access to port 8080',
            ingress=[
                { 'protocol': 'tcp', 'from_port': 8080, 'to_port': 8080, 'cidr_blocks': ['0.0.0.0/0'] },
                { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
            ])

server = aws.ec2.Instance('webserver',
    instance_type=size,
    vpc_security_group_ids=[group.id], 
    ami=ami.id,
    subnet_id=my_subnet.id,
    user_data = user_data,
    tags = { "Name": "Pulumi" },
    )
    

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)


