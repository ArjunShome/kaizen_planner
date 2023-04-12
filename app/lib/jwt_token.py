from datetime import datetime, timedelta

import jwt
from flask import current_app as flask_app


class JwtToken:
    @staticmethod
    def create_jwt_token(ip_address, expiration, user_id=None):
        flask_app.logger.info(f'Generating JWT token for IP {ip_address} and expiration limit as {expiration} seconds')
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(seconds=expiration),
                'iat': datetime.utcnow(),
                'sub': str(ip_address)
            }

            if user_id:
                user_id = str(user_id)
                flask_app.logger.info(f'Generating auth token for user {user_id}')
                payload['user_id'] = user_id

            return jwt.encode(
                payload,
                flask_app.config.get('JWT_SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as ex:
            return ex

    @staticmethod
    def verify_token(token, ip_address=None):
        flask_app.logger.info(f'Verifying the token {token}')
        try:
            payload = jwt.decode(token, flask_app.config.get('JWT_SECRET_KEY'))
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False

        if ip_address and ip_address != payload['sub']:
            return False

        return payload
