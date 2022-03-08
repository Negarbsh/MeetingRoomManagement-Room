import enum


class Response(enum.Enum):
    unauthorized = 401
    access_forbidden = 403
    invalid_request = 406
    ok = 200
    bad_request = 400
    created = 201
    updated = 200  # todo find it out
    method_not_found = 405
