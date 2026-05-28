import boto3

client = boto3.client("dynamodb")
client.delete_item(
    TableName='faculties',
    Key={
        'faculity_id': {'S': 'F001'},
        'qualification': {'S': 'PhD'}
    }
)
print("Item Deleted successfully")