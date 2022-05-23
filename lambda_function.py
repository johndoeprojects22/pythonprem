# lambda function Template
import json

def lambda_handler(event, context):
  #exec(open("INSERT").read())
  command = "python3 " + "INSERT"
  res = subprocess.check_output(command, shell=True).strip()
  news = str(res,"utf-8")
  return {
        "statusCode": 200,
        'body': json.dumps(news)        
  }
