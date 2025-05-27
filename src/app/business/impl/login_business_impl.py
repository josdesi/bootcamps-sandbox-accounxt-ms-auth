import os
import jwt
import uuid
from decimal import Decimal
from datetime import datetime, timedelta
from app.repository.users_auth_repository import UsersAuthRepository
from app.business.login_business import ILoginBusiness
from app.model.login_model import LoginCredentials
from app.model.jwt_auth import JWTAuth

class LoginBusiness(ILoginBusiness):
    def __init__(self, auth_repository: UsersAuthRepository):
        self.auth_repository = auth_repository
        self.jwt_auth = JWTAuth()

    def authenticate(self, credentials: LoginCredentials):
        user = None
        if self.jwt_auth.is_email(credentials.username):
            user = self.auth_repository.get_user_by_email(credentials.username)                    
        else:
            user = self.auth_repository.get_user_by_username(credentials.username)
        self.jwt_auth.validate_password(credentials.password, user.get('password'))
        token = self.jwt_auth.generate_token(user)
        return self.jwt_auth.build_auth_response(token)


    
    def cognito_authenticate(self, credentials: LoginCredentials):
        region = 'us-east-1'
        client_id = '1egqgfm5ljhg07qh18fva5ns6u'
        
        client = boto3.client('cognito-idp', region_name=region)

        try:
            response = client.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': credentials.username,
                    'PASSWORD': credentials.password
                },
                ClientId=client_id
            )
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
            raise Exception(e.response['Error']['Message'])
            