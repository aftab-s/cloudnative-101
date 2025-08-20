# Using AWS Lambda

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.

## Creating a Simple Lambda Function

Here's a basic example of how to create a "Hello, World!" Lambda function using Python.

### 1. Write the Function Code

Create a file named `lambda_function.py` with the following content:

```python
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

### 2. Create a Deployment Package

Zip the Python file:

```bash
zip function.zip lambda_function.py
```

### 3. Create the Lambda Function

Use the AWS CLI to create the Lambda function. You'll need to provide an execution role with the necessary permissions.

```bash
aws lambda create-function --function-name my-hello-world-function \
--runtime python3.8 \
--role arn:aws:iam::123456789012:role/lambda-ex \
--handler lambda_function.lambda_handler \
--zip-file fileb://function.zip
```

Replace `123456789012` with your AWS account ID and `lambda-ex` with the name of your execution role.

### 4. Invoke the Function

You can invoke the function from the command line:

```bash
aws lambda invoke --function-name my-hello-world-function output.txt
```

The output of the function will be saved in `output.txt`.
