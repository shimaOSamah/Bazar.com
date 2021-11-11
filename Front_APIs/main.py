from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
import requests
import json 

def foo():
    return request.json['inputVar']

app = Flask(__name__)
CORS(app)
CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)

def login():
  return jsonify({'success': 'ok'})
    

@app.route('/search/<cat>')
def search_api(cat):  
    r = requests.get("http://192.168.187.130:5000/query/search/"+cat)
    return r.text

@app.route('/search')
def search():
    r = requests.get("http://192.168.187.130:5000/query/search")
    return r.text

@app.route('/info/<id>')
def info_api(id):  
    r = requests.get("http://192.168.187.130:5000/query/info/"+id)
    return r.text

@app.route('/info')
def info():  
    r = requests.get("http://192.168.187.130:5000/query/info")
    return r.text

@app.route('/purchase/<id>', methods=["PUT"])
def purchase_api(id): 
    r = requests.put("http://192.168.187.129:5000/purchase/"+id) 
    js = r.json()
    return js["status"]

@app.route('/purchase', methods=["PUT"])
def purchase():  
    return "fail, Item ID is needed"


if __name__ == "__main__":
    app.run(debug=True, host="192.168.187.128") 
