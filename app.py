# app.py
from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

# countries = {
#     "Thailand":{"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
#     "Australia":{"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
#     "Egypt":{"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
# }

# def _find_next_id():
#     # return max(country["id"] for country in countries) + 1
#     return len(countries.keys())+1

@app.get("/")
def hello():
    return "Hello World!"

# @app.post("/helloname")
# def hello_name():
#     if request.is_json:
#         data = request.get_json()
#         name = data['name']
#         print(name)
#         return f"Hello {name}!"
#     return {'string':'Empty Json'}

# @app.get("/countries")
# def get_countries():
#     return jsonify(countries)

@app.get("/time")
def time():
    return str(datetime.datetime.now())

# @app.post("/countries")
# def add_country():
#     print('request ', request)
#     if request.is_json:
#         country = request.get_json()
#         if country['name'] not in countries.keys():
#             country["id"] = _find_next_id()
#             countries[country['name']] = country
#             return countries, 201
#     return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    # USE THIS ONE
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    ## NOT THESE -- Though not exactly sure why these dont work? Maybe it needs the 
    ## os.environ to get the correct path in the containter?
    # app.run(debug=False, port='5000')
    # app.run(debug=False, port=int(os.environ.get("PORT", 5000)))
