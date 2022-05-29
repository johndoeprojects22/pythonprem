import os
import random
import string
import boto3 
import sys 
import subprocess

# initializing size of string 


N = 8
  
# using random.choices()
# generating random strings 
res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))

stacks = subprocess.check_output('aws cloudformation list-stack-sets --stacks "ACTIVE"', shell=True) 

content = str(stacks)

if 'pyprem' in content:
  print(content)

else:
#could be anything here.
  command = "aws s3api create-bucket --bucket " + res + " --region us-east-1"
  os.system(command)

  # Read in the file
  with open('serverless.yaml', 'r') as file:
    filedata = file.read()

  fname = res

  # Replace the target string
  filedata = filedata.replace("INSERT", fname)

  # Write the file out again
  with open('serverless.yaml', 'w') as file:
    file.write(filedata)


  os.system("more serverless.yaml")



  destfile = res +"/"

  command2 = "aws s3 cp hello.zip s3://"+destfile

  os.system(command2)



  os.system("aws cloudformation deploy --template-file serverless.yaml --stack-name pyprem")


