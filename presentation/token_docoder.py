import jwt


def decode_token(encoded_token):
    token_key = 'Negar'  # todo
    try:
        return jwt.decode(encoded_token, token_key, algorithms="HS256")
    except BaseException as e:
        print(e)
        return None

