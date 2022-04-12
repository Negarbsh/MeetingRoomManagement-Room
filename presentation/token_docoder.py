import os

import jwt


def decode_token(encoded_token):
    token_key = os.environ['TOKEN_KEY']
    try:
        return jwt.decode(encoded_token, token_key, algorithms="HS256")
    except BaseException as e:
        print(e)
        return None
