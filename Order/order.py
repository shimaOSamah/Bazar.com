from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import json
import requests

def foo():
    return request.json['inputVar']

app = Flask(__name__)
CORS(app)
CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)

def login():
  return jsonify({'success': 'ok'})
    

@app.route('/purchase/<id>', methods=['PUT'])
def search_api(id):  
    r = requests.get('http://192.168.187.130:5000/query/info/'+id)
    js = r.json()

    if(len(js)==0):
        return {"status":"fail, NO such book"}

    q = js[0]["quantity"]
    if(int(q) > 0):
        rs = requests.put('http://192.168.187.130:5000/update/'+id)
        return rs.text

    return {"status":"fail, all soled"}

if __name__ == "__main__":
    app.run(debug=True, port=5003, host="192.168.187.129") 


