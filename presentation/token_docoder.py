import jwt


def decode_token(encoded_token):
    token_key = 'Negar'  # todo
    try:
        return jwt.decode(encoded_token, token_key, algorithms="HS256")
    except BaseException as e:
        print(e)
        return None

# function decode_token(req) {
#     const token = req.header('token')
#     let decoded_token
#     try {
#         jwt.verify(token, process.env.TOKEN_KEY, {}, function (err, decoded) {
#             if (err) throw new Error(err)
#             decoded_token = decoded //token info is returned in 'decoded'
#         })
#         return decoded_token
#     } catch (e) {
#         return null
#     }
# }

