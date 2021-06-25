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


group = aws.ec2.SecurityGroup('pulumi_allow_8080',
            description='Enable access to port 8080',
            ingress=[
                { 'protocol': 'tcp', 'from_port': 8080, 'to_port': 8080, 'cidr_blocks': ['0.0.0.0/0'] }
            ])

server = aws.ec2.Instance('webserver',
    instance_type=size,
    vpc_security_group_ids=[group.id], 
    ami=ami.id,
    user_data = user_data,
    tags = { "Name": "Pulumi" },
    )
    

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)