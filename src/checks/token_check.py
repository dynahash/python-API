import json

token_fix = json.load(open("../configs.json"))

def checkToken(token):
    if token == token_fix["token"]:
        return {True: token_fix["token"]}
    else:
        return {False: 'You do not have the permission for use this route'}
