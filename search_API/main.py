from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import request
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
    

@app.route('/info')
def get_daily_summary():  
   
    jsonArray = []
    return json.dumps(jsonArray,indent=4)


@app.route('/purchase')
def get_test_statistics():  

    jsonArray = []
    return json.dumps(jsonArray,indent=4)

    

if __name__ == "__main__":
    app.run(debug=True ) 
