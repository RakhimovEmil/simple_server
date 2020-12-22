from flask import Flask, request, make_response
import requests
import os 
import json

app = Flask(__name__)
hosts = []

def url(key):
  host = hosts[len(key) % len(hosts)]
  return f'http://{host}/storage/' + key

@app.route("/<filename>", methods=['GET', 'PUT', 'DELETE'])
def r(filename):
  if request.method == 'GET':
    res = requests.get(url(filename))
    if res.status_code == 200:
      return make_response(res.text, res.status_code)
    else:
      return make_response("", res.status_code)
    
  if request.method == 'PUT':
    req = request.get_json()
    res = requests.put(url(filename), json=req)
    return make_response("", res.status_code)
  
  if request.method == 'DELETE':
    res = requests.delete(url(filename), data=filename)
    return make_response("", res.status_code)

if __name__ == "__main__":
    hosts = os.getenv('HOSTS').split(',')
    app.run(host='0.0.0.0', port=8082)
