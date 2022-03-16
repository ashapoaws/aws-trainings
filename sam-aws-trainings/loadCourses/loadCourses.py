import boto3
import json

table_name = 'Trainings'

# Local ddb
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
dynamodb_client = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

# Ddb service
# dynamodb = boto3.resource('dynamodb')
# dynamodb_client = boto3.client('dynamodb')


# Create a table if it not exists 
def create_ddb_table(ddb_table_name):
    table = dynamodb.create_table(
        TableName=ddb_table_name,
        KeySchema=[
            {
                'AttributeName': 'CategoryId',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'CourseId',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'CategoryId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'CourseId',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table    

# Load some sample data into DDB table
def load_courses(courses):
    table = dynamodb.Table(table_name)
    for course in courses:
        CategoryId = course['CategoryId']
        CourseId = int(course['CourseId'])
        CategoryName = course['CategoryName']
        CourseName = course['CourseName']
        Level = course['Level']
        Duration = int(course['Duration'])
        CourseOutline = course['CourseOutline']
        table.put_item(Item=course)
    print(table.item_count, "items loaded")

# Get list of DynamoDB tables in current region
existing_tables = dynamodb_client.list_tables()['TableNames']

# Create table if it doesn't exist
if table_name not in existing_tables:
    print("Table doesn't exist and will be created...")
    table = create_ddb_table(table_name)
    table.wait_until_exists()
    print("DynamoDB table with the name", table.table_name, "was created")
else:
    print("Table already exists")

# Load data from file
with open('loadCourses/courses_test.json') as json_file:
    courses_list = json.load(json_file)
load_courses(courses_list)





