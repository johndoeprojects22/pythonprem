# lambda function Template
import json

def lambda_handler(event, context):
  exec(open("INSERT").read())
  return {
        "statusCode": 200,
        'body': json.dumps('Lambda Deployed')        
  }
