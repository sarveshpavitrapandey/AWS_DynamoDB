import boto3

client = boto3.client("dynamodb")

response = client.put_item(
    TableName='faculties',
    Item={
        'faculity_id': {'S': 'F003'},       
        'qualification': {'S': 'MBA'},      
        'faculty_name': {'S': 'Mr. Meghan Adhav'},
        'dept': {'S': 'Business Administrative'}
    }
)
print("Item put successfully")