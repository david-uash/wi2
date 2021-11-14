#!/usr/local/bin/python

from datetime import datetime,timezone
import pytz
import boto3 


ISR = pytz.timezone('Asia/Jerusalem')
session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="us-east-2",
)


machineToShut = []
ec2 = session.resource('ec2')
ec2client = session.client('ec2', region_name="us-east-2")
for instance in ec2.instances.all():
#  print(instance)
#  print("id:",instance.id)
#  print("type",instance.instance_type)
#  print("publicIP",instance.public_ip_address)
#  print("tags",instance.tags)
  for mytag in instance.tags:
    if((mytag['Key']=="timeToShut")):
       mytime = mytag['Value']
       myhour = mytime.split(":")[0]
       myminuts = mytime.split(":")[1]
       now = datetime.now(timezone.utc)
       ISR_now = now.astimezone(ISR)
       dateToShutEC2 = ISR_now.replace(hour=int(myhour), minute=int(myminuts))
       if(dateToShutEC2 > ISR_now):
           print("in the futher")
       else:
           print("in the past")
           print("shut this machine",instance)
           #ec2client.stop_instances(InstanceIds=[instance.id])
  print("###########################################")


print("hello world")

