from flask import Flask
from flask import jsonify
from flask import request
from mercury_dl import YTDLSession

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_data():
    args = request.json['args']
    user = request.json['user']
    session = YTDLSession(args, user)
    execution = session._download()
    if execution == "Success!":
        return jsonify({"status":200})
    else:
        return jsonify({"status":execution})