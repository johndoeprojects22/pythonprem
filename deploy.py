import os
import random
import string
import boto3 
import sys 
import subprocess

# initializing size of string 


  
# using random.choices()
# generating random strings 



stacks = subprocess.check_output('aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE', shell=True) 

content = str(stacks)

if 'pyprem' in content:
  print(content)
  
  
  s3 = boto3.resource('s3')
  buckets = s3.buckets.all()
  print(type(buckets))
  for bucket in buckets:
     if 'pyprem' in bucket.name:
        fname = str(bucket.name)
 
  N = 3

  version = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
  
  package = "hello"+version+".zip"
  fname="pyprem2022"
  
  os.system("aws s3 rm "+"s3://pyprem2022/"+"hello.zip")
  os.system("zip "+package+"lambda_function.py hello.py")
  os.system("aws s3 cp "+package+" s3://"+fname+"/")

  os.system("aws s3 list-objects --bucket pyprem2022")
  
  
  with open('serverless.yaml', 'r') as file:
    filedata = file.read()
 
  #fname = target

  # Replace the target string
  filedata = filedata.replace("INSERT", "pyprem2022")

  # Write the file out again
  with open('serverless.yaml', 'w') as file:
    file.write(filedata)

  
  with open('serverless.yaml', 'r') as file1:
    filedata2 = file.read()
 
  
  
  filedata2 = filedata2.replace("hello.zip", package)
  with open('serverless.yaml', 'w') as file1:
    file.write(filedata2)

  os.system("more serverless.yaml")


  
  res = "serverless"+version+".yaml"
  os.rename('serverless.yaml',res)
  
  #destfile = fname +"/"

  #command2 = "aws s3 cp hello.zip s3://"+destfile

  #os.system(command2)
  
  print("flag 2")
  
  os.system("aws cloudformation update-stack --stack-name pyprem --template-body file://"+res)

  
 
  
  
else:
  
  N = 4

  res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))

  target = "pyprem2022"
#could be anything here.
  command = "aws s3api create-bucket --bucket " + target + " --region us-east-1"
  os.system(command)

  # Read in the file
  with open('serverless.yaml', 'r') as file:
    filedata = file.read()

  fname = target
 # print("===================")
  #print(fname)
  # Replace the target string
  filedata = filedata.replace("INSERT", fname)

  # Write the file out again
  with open('serverless.yaml', 'w') as file:
    file.write(filedata)


 # os.system("more serverless.yaml")

  #os.system("ls")
  print("HERE")
  destfile = target +"/"
  
  command2 = "aws s3 cp hello.zip s3://"+destfile

  os.system(command2)



  os.system("aws cloudformation deploy --template-file serverless.yaml --stack-name pyprem")


