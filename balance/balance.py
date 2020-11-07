from flask import Flask, request, make_response
import requests
import json

app = Flask(__name__)

@app.route("/<filename>", methods=['GET', 'PUT', 'DELETE'])
def r(filename):
  if len(filename) > 6:
    url = 'http://localhost:8080/storage/' + filename
  else:
    url = 'http://localhost:8081/storage/' + filename
  if request.method == 'GET':
    res = requests.get(url)
    if res.status_code == 200:
      return make_response(res.text, res.status_code)
    else:
      return make_response("", res.status_code)
  if request.method == 'PUT':
    req = request.get_json()
    res = requests.put(url, json=req)
    return make_response("", res.status_code)
  if request.method == 'DELETE':
    res = requests.delete(url, data=filename)
    return make_response("", res.status_code)

if __name__ == "__main__":
    app.run(port=8082)
