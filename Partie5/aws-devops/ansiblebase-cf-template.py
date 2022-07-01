"""Generating CloudFormation template."""
from ipaddress import ip_network

from ipify import get_ip

from troposphere import (
    Base64,
    ec2,
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Template,
)

ApplicationName = "helloworld"
ApplicationPort = "3000"

GithubAccount = "EffectiveDevOpsWithAWS"
GithubAnsibleURL = "https://github.com/{}/ansible".format(GithubAccount)

AnsiblePullCmd = \
    "/usr/local/bin/ansible-pull -U {} {}.yml -i localhost".format(
        GithubAnsibleURL,
        ApplicationName
    )

PublicCidrIp = str(ip_network(get_ip()))

t = Template()

t.add_description("AWS et DEVOPS : application Web HelloWorld")

t.add_parameter(Parameter(
    "KeyPair",
    Description="Nom d'une EC2 KeyPair existante vers SSH",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="doit être le nom d'une EC2 KeyPair existante.",
))

t.add_resource(ec2.SecurityGroup(
    "SecurityGroup",
    GroupDescription="Autoriser l'accès SSH et TCP/{}".format(ApplicationPort),
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp=PublicCidrIp,
        ),
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=ApplicationPort,
            ToPort=ApplicationPort,
            CidrIp="0.0.0.0/0",
        ),
    ],
))

ud = Base64(Join('\n', [
    "#!/bin/bash",
    "yum install --enablerepo=epel -y git",
    "pip install ansible",
    AnsiblePullCmd,
    "echo '*/10 * * * * {}' > /etc/cron.d/ansible-pull".format(AnsiblePullCmd)
]))

t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-a4c7edb2",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
))

t.add_output(Output(
    "InstancePublicIp",
    Description="IP publique de notre instance.",
    Value=GetAtt("instance", "PublicIp"),
))

t.add_output(Output(
    "WebUrl",
    Description="Point de terminaison de l'application",
    Value=Join("", [
        "http://", GetAtt("instance", "PublicDnsName"),
        ":", ApplicationPort
    ]),
))

print t.to_json()
