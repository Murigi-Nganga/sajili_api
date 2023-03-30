import jwt
import pytz
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv('SECRET_KEY')
hash_algorithm = os.getenv('HASH_ALGORITHM')

tz = pytz.timezone('Africa/Addis_Ababa')      #? Check if already catered for in config.settings

def generate_access_token(target_string):
    payload = {
        'exp': tz.localize(datetime.utcnow() + timedelta(minutes=100)),
        'iat': tz.localize(datetime.utcnow()),
        'sub': target_string
    }
    access_token = jwt.encode(payload, secret, algorithm=hash_algorithm)
    return access_token


def decode_access_token(access_token):
    try:
        payload = jwt.decode(access_token, 'secret', algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'access_token_expired'
    except jwt.InvalidTokenError:
        return 'invalid_access_token'