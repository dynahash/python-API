from flask import Flask, request
from src.checks.token_check import checkToken

app = Flask('WannaEat')

@app.route("/primaryRoute", methods=["GET"])
def primary_route():
    token = request.args.get('token')
    check = checkToken(token)

    if False in check.keys():
        return check[False]  # if error, return that string
    dads = {check[True]:
                {'hello word': '123'}
            }

    return dads


app.run()
