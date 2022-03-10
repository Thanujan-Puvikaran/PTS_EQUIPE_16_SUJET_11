class raiseError:
    JSONERROR = "Failed to decode JSON object: Expecting value"
    JSONMESSAGE = (
        "You made a mistake, "
        "if you do not know a particular value "
        "just give an empty string if it is a string type variable and 0 "
        "if it is an integer or float type variable"
    )
    TYPEERROR = "TypeError"
    TYPEMESSAGE = "Wrong variable type, check it carefully"


class credentials:
    API_KEY = "a7a0813f3d0ae3a4c26bf99545474eae"
    API_BASE_URL = "https://api.themoviedb.org/3"
