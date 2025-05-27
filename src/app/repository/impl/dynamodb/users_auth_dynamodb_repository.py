import os
import boto3
from typing import Optional, Dict
from app.repository.users_auth_repository import UsersAuthRepository

class UsersAuthDynamoDBRepository(UsersAuthRepository):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',
            region_name=os.getenv('AWS_REGION', 'us-east-1'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID_'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY_'))
        self.table = self.dynamodb.Table(os.getenv('DYNAMODB_TABLE_NAME_AUTH'))

    def get_user_by_email(self, email: str) -> Optional[Dict]:
        response = self.table.get_item(Key={'email': email})
        user = response.get('Item')
        if not user:
            raise Exception("User not found")
        return user

    def get_user_by_username(self, username: str) -> Optional[Dict]:
        if not 'GET_USER_BY_USERNAME' in os.getenv('CACHE_FLAGS', '').split("|"):
            response = self.table.scan(
                FilterExpression='username = :username',
                ExpressionAttributeValues={
                    ':username': username
                }
            )
            if not response['Items']:
                raise Exception("User not found")
            return response['Items'][0]
        
