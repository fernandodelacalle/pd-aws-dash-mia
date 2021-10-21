import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='MARKET_DATA',
    KeySchema=[
        {
            'AttributeName': 'VALOR',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'TIME',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'VALOR',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'TIME',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
