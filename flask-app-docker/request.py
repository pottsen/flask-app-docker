import requests
import json

# url = 'http://127.0.0.1:5000/helloname'  # localhost and the defined port + endpoint
url = 'https://pottsen-atrium-hw2.azurewebsites.net/helloname'
body = {
    "name": "Peter"
}
response = requests.post(url, json=body)
print(response.text)

# url = 'http://127.0.0.1:5000/countries'  # localhost and the defined port + endpoint
url = 'https://pottsen-atrium-hw2.azurewebsites.net/countries'
body = {
    "id": 1,
    "name": "Montana",
    "capital": "Helena", 
    "area": 1000000
}
response = requests.post(url, json=body)
print(response.text)

