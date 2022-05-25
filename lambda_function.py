# lambda function Template
import json
import subprocess

def lambda_handler(event, context):
  #exec(open("hello.py").read())
  command = "python3 " + "hello.py"
  res = subprocess.check_output(command, shell=True).strip()
  news = str(res,"utf-8")
  content = news.replace("\n","<br>")
  print(content)
  response_body = "<html><body><h1>"+content+"</h1></body></html>"
    
    
    
  return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
  }
}
