# app.py
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

countries = {
    "Thailand":{"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    "Australia":{"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    "Egypt":{"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
}

def _find_next_id():
    # return max(country["id"] for country in countries) + 1
    return len(countries.keys())+1

@app.get("/")
def hello():
    return "Hello World!"

@app.post("/helloname")
def hello_name():
    if request.is_json:
        data = request.get_json()
        name = data['name']
        print(name)
        return f"Hello {name}!"
    return {'string':'Empty Json'}

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/time")
def time():
    return str(datetime.datetime.now())

@app.post("/countries")
def add_country():
    print('request ', request)
    if request.is_json:
        country = request.get_json()
        if country['name'] not in countries.keys():
            country["id"] = _find_next_id()
            countries[country['name']] = country
            return countries, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True, port='5000')


