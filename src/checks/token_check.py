from decouple import config


def checkToken(token_parm): # function token validator
    token = config("TOKEN_ADMIN")  # Collect data from .env file

    if token_parm == token:
        return {True: token}
    else:
        return {False: 'You do not have the permission for use this route'}
