# creates or updates the lambda function
import os
import random
import string
import boto3 
import sys

accesskey = sys.argv[1]
secretkey = sys.argv[2]

client = boto3.client('iam',aws_access_key_id=accesskey,aws_secret_access_key=secretkey)
roles = client.list_roles()
Role_list = roles['Roles']
flag = 0
for key in Role_list:
    if key['RoleName'] == "lambda-example-role":
        flag = 1

print(flag)


if flag == 1:
    command1 =  "aws lambda update-function-code --function-name pythonprem-lmda --zip-file fileb://pythonprem.zip"
    os.system(command1)

else:
    os.system("wget https://raw.githubusercontent.com/johndoeprojects22/pythonprem/main/trust-policy.json")
    command2 = "aws iam create-role --role-name lambda-example-role --assume-role-policy-document file://trust-policy.json"
    os.system(command2)
    command3 = "aws iam attach-role-policy --role-name lambda-pythonprem1-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    os.system(command3)
    #iam = boto3.client('iam')
    user = client.get_user()
    aws_account_id =  user['User']['Arn'].split(':')[4]
    command4 = "aws lambda create-function --function-name pythonprem1-lmda --handler lambda_function.lambda_handler --runtime python3.8 --zip-file fileb://pythonprem.zip --role"
    arn = "arn:aws:iam::"+aws_account_id+":role/lambda-example-role"
    net = command4 + " " + arn
    os.system(net)


    
    ##print(aws_account_id)
    
    #print(aws_account_id)
    #print(key['RoleName'])
    #print(key['Arn'])

#res = ''.join(random.choice(letters) for i in range(5)) 

#rolename = "lambda-" +"pythonprem"+res
#command1 = "aws iam create-role --role-name " +rolename+ " --assume-role-policy-document file://trust-policy.json"
#command2 = "aws iam attach-role-policy --role-name " +rolename + " --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
#os.system(command1)
#os.system(command2)
