import enum


class Office(enum.Enum):
    TEHRAN = 'Tehran'
    MASHHAD = 'Mashhad'
    SHIRAZ = 'Shiraz'


def get_office_key(given_value):
    for key in Office:
        if key.value == given_value:
            return key
    return None
