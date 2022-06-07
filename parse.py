import sys
import boto3
import os
import time


stacks = subprocess.check_output('aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE', shell=True) 

content = str(stacks)

if 'vpcendpoint' not in content:
  os.system("aws cloudformation deploy --template-file endpoint.yaml --stack-name vpcendpoint")


time.sleep(15)  

# Read in the file
with open('lambda_function.py', 'r') as file:
  filedata = file.read()

fname = sys.argv[1]

# Replace the target string
filedata = filedata.replace("INSERT", fname)

# Write the file out again
with open('lambda_function.py', 'w') as file:
  file.write(filedata)

  

response = client.describe_stack_resource(
    StackName="vpcendpoint",
    LogicalResourceId="APIEndpoint" #Logical ID in you template
)
  
print(response)


#filedata = filedata.replace("INSERT2",)
#with open('serverless.yaml','w') as file:
#  file.write(filedata)
