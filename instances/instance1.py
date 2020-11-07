from flask import Flask, make_response, request
import json

app = Flask(__name__)

d = {}

@app.route("/storage/<filename>", methods=['GET'])
def get(filename):
    if filename in d:
        ans = make_response(d[filename], 200)
        return ans
    else:
        return make_response("", 404)

@app.route("/storage/<filename>", methods=['PUT'])
def put(filename):
    if request.method == 'PUT':
        req = request.get_json()
        if req == None:
            return make_responce("", 400)
        d[filename] = req  
        return make_response("", 201)

@app.route("/storage/<filename>", methods=['DELETE'])
def delete(filename):
    if filename in d:
        del d[filename]
    return make_response("", 204)
    
if __name__ == "__main__":
    app.run(port=8080)
