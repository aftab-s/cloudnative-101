# Using AWS Lambda

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.

## Creating Lambda Functions Using AWS Console

### 1. Create a Function
1. Sign in to AWS Management Console
2. Navigate to Lambda service
3. Click "Create function"
4. Choose one of the following:
   - Author from scratch
   - Use a blueprint
   - Container image
   - Browse serverless app repository

### 2. Configure Basic Settings
1. Enter function name
2. Choose runtime (e.g., Python 3.8, Node.js 14.x)
3. Choose or create an execution role
4. Click "Create function"

### 3. Write Function Code
In the Lambda console code editor:
```python
import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

### 4. Test the Function
1. Click "Test" button
2. Create a new test event
3. Enter event name
4. Provide JSON test data
5. Click "Test" to run

### 5. Monitor Function
- View CloudWatch Logs
- Check metrics in the Monitoring tab
- View execution results

## Using AWS CLI

For automation and CI/CD pipelines, you can use CLI:

### 1. Create Deployment Package
```bash
zip function.zip lambda_function.py
```

### 2. Create Function
```bash
aws lambda create-function \
--function-name my-hello-world-function \
--runtime python3.8 \
--role arn:aws:iam::123456789012:role/lambda-ex \
--handler lambda_function.lambda_handler \
--zip-file fileb://function.zip
```

### 3. Invoke Function
```bash
aws lambda invoke \
--function-name my-hello-world-function output.txt
```

## Best Practices
1. Keep functions focused and small
2. Handle errors appropriately
3. Use environment variables for configuration
4. Monitor execution time and memory usage
5. Clean up resources when done

## Common Use Cases
- API backends
- Data processing
- Scheduled tasks
- Real-time file processing
- Stream processing
- Web applications
