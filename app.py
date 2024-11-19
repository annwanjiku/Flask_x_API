from flask import Flask, jsonify, request
import requests
import json
from funcs import getRandomNumber

app = Flask(__name__)

@app.route("/")
def landingPage():
    return "Welcome to the landing page"

@app.route("/jikan")
def getSynopsis():
    random_number = getRandomNumber()
    url = f'https://api.jikan.moe/v4/anime/{random_number}'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        data = result['data']['synopsis']
        return f"Episode {random_number} \n\n {data}"
    else:
        return "Error fetching synopsis ",response.status_code

if __name__ == "__main__":
    app.run(port=5000,debug=True)