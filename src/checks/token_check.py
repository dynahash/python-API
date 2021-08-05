import json

token_fix = json.load(open("../configs.json")) # Collect data from .json file


def checkToken(token): # function token validator
    if token == token_fix["token"]:
        return {True: token_fix["token"]}
    else:
        return {False: 'You do not have the permission for use this route'}
