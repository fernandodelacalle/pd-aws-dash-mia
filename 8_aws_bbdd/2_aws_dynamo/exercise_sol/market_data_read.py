import pandas as pd
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MARKET_DATA')

response = table.query(
    KeyConditionExpression=Key('VALOR').eq('SAN')
)

print(response['Items'])

df = pd.DataFrame(response['Items'])
print(df)
