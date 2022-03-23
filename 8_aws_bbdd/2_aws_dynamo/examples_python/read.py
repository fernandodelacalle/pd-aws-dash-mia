import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

try:
    response = table.get_item(Key={'year': 2015, 'title': "The Big New Movie"})
except ClientError as e:
    print(e.response['Error']['Message'])

print(response['Item'])

