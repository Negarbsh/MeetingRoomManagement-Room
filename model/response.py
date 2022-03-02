import enum


class Response(enum.Enum):
    access_forbidden = 403
    invalid_request = 406
    ok = 200
    bad_request = 400
    created = 201
    updated = 204  # todo find it out
