def lambda_handler(event, context):
    name = event.get("name", "Guest")
    return {
        'statusCode': 200,
        'body': f'Hello {name}, welcome to AWS Lambda!'
    }