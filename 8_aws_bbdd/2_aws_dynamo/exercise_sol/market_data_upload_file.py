import pandas as pd
import boto3
from decimal import Decimal


data = pd.read_csv('../../../data_exercises/market_data/market_data_proc.csv')
print(data.shape)
print(data.columns)

dynamodb = boto3.resource('dynamodb')

records = data.to_dict(orient='records')
for record in records:
    print(record)
    record['PRECIO'] = str(record.get('PRECIO'))
    print(record)
    table = dynamodb.Table('MARKET_DATA')
    response = table.put_item(
        Item=record
    )
