import os
import jwt
import uuid
import hashlib
from decimal import Decimal
from datetime import datetime, timedelta
import re

class JWTAuth:
    def __init__(self):
        self.JWT_EXPIRATION_MINUTES = int(os.getenv('JWT_EXPIRATION_MINUTES', '60'))
        self.secret_key = os.getenv('JWT_SECRET_KEY')
        self.email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def is_email(self, email):
        if not self.email_regex.match(email):
            return False
        return True

    def validate_password(self, credentials_password, stored_password):
        if not stored_password:
            raise Exception("Invalid credentials")
        hashed_password = hashlib.md5(credentials_password.encode()).hexdigest()
        if hashed_password != stored_password:
            raise Exception("Invalid credentials")
        return True

    def generate_token(self, user):
        cleaned_user = {k: int(v) if isinstance(v, Decimal) else v for k, v in user.items() if k != 'password'}
        data = {
            'user': cleaned_user,
            'exp': datetime.utcnow() + timedelta(minutes=self.JWT_EXPIRATION_MINUTES)
        }
        return jwt.encode(data, self.secret_key, algorithm="HS256")

    def build_auth_response(self, token):
        return {
            "ChallengeParameters": {},
            "AuthenticationResult": {
                "AccessToken": token,
                "ExpiresIn": self.JWT_EXPIRATION_MINUTES * 60,
                "TokenType": "Bearer",
                "RefreshToken": "",
                "IdToken": ""
            },
            "ResponseMetadata": {
                "RequestId": str(uuid.uuid4()),
                "HTTPStatusCode": 200,
                "HTTPHeaders": {
                    "date": datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"),
                    "content-type": "application/x-amz-json-1.1",
                    "content-length": "3948",
                    "connection": "keep-alive",
                    "x-amzn-requestid": "aead30fa-694f-425f-96f6-7d78389cbe79"
                },
                "RetryAttempts": 0,
                "WebStreamingClient": {
                    "Key": os.getenv('WEB_STREAMING_CLIENT_AWS_ACCESS_KEY_ID'),
                    "Value": os.getenv('WEB_STREAMING_CLIENT_AWS_SECRET_ACCESS_KEY')
                }
            }
        }