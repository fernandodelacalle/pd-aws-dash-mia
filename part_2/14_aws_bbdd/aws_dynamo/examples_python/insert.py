import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies')

response = table.put_item(
    Item={
        'year': 2015,
        'title': "The Big New Movie",
        'info': {
            'plot': "Nothing happens at all.",
            'rating': 0
        }
    }
)
