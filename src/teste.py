import requests

api = requests.get("http://127.0.0.1:5000/primaryRoute?token=OlCnkK9wmRImhwN")

json = api.json()
