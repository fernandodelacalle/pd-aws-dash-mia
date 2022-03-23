import json

def lambda_handler(event, context):
    # TODO implement
    
    params = event.get('multiValueQueryStringParameters')
    
    a = params.get('a')[0]
    b = params.get('b')[0]
    result = int(a) + int(b)
    
    return {
    'statusCode': 200,
    'body': result
    }
