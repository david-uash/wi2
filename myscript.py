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

print("hello world")

