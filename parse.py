import sys
import boto3
import os
import time
import subprocess


stacks = subprocess.check_output('aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE', shell=True) 

content = str(stacks)

print(content)

if 'vpcendpoint' not in content:
  os.system("aws cloudformation deploy --template-file endpoint.yaml --stack-name vpcendpoint")


# Read in the file
with open('lambda_function.py', 'r') as file:
  filedata = file.read()

fname = sys.argv[1]

# Replace the target string
filedata = filedata.replace("INSERT", fname)

# Write the file out again
with open('lambda_function.py', 'w') as file:
  file.write(filedata)

  
client = boto3.client('cloudformation')

response = client.describe_stack_resource(
    StackName="vpcendpoint",
    LogicalResourceId="APIEndpoint" #Logical ID in you template
)

content = response['StackResourceDetail']['PhysicalResourceId']
print(content)


filedata = filedata.replace("HERE",content)
with open('serverless.yaml','w') as file:
  file.write(filedata)

  
os.system("more serverless.yaml")
