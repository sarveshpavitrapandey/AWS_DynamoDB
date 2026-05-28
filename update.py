import boto3

client = boto3.client("dynamodb")
response = client.update_item(
    TableName='faculties',
    Key={
        'faculity_id': {'S': 'F001'},
        'qualification': {'S': 'PhD'}
    },
    UpdateExpression="SET dept = :new_dept",
    ExpressionAttributeValues={
        ':new_dept': {'S': 'Mechanical Engineering'}
    }
)
print("Item updated successfully")