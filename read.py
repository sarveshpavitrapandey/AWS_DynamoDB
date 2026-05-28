import boto3

client = boto3.client("dynamodb")

response = client.get_item(
    TableName='faculties',
    Key={
        'faculity_id': {'S': 'F001'},
        'qualification': {'S': 'PhD'}
    }
)
print(response.get('Item'))