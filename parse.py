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

stacks = subprocess.check_output('aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE', shell=True) 
if 'pyprem' in content:
  print("flag HERE HERE")
  N = 3

  version = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
  
  package = "hello"+version+".zip"
  fname="pyprem2022"
  os.system("aws s3 rm "+"s3://pyprem2022/"+"hello.zip")
  os.system("zip "+package+" lambda_function.py hello.py")
  os.system("aws s3 cp "+package+" s3://"+fname+"/")
#client = boto3.client('cloudformation')

#response = client.describe_stack_resource(
#    StackName="vpcendpoint",
#    LogicalResourceId="APIEndpoint" #Logical ID in you template
#)

#content = response['StackResourceDetail']['PhysicalResourceId']
#print(content)


# Read in the file
  with open('serverless.yaml', 'r') as file1:
    filedata1 = file1.read()


  filedata1 = filedata1.replace("hello.zip",package)
  with open('serverless.yaml','w') as file1:
    file1.write(filedata1)
   
  
#os.system("more serverless.yaml")
