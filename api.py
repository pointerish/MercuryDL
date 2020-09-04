import hashlib

# Flask Imports
from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file

# utils.py Imports 

from utils import *

# MercuryDL Imports

from mercury_dl import YTDLSession


app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download() -> dict:
    """This function downloads the file from the specified source

    Returns:
        dict: A dict containing either a file name as key and bin file as value
              or a dict containing `status` as key and the the YouTube-DL error message as value.
    """
    session = YTDLSession(request.json['args'], request.json['api_token'])
    execution = session._download()
    if execution['msg'] == 'Success!':
        return send_file(f'./{execution["file"]}', attachment_filename=execution['file'])
    else:
        return jsonify({'status':execution['msg']})


@app.route('/register', methods=['POST'])
def register() -> dict:
    """This function registers the user and triggers email API Key Send procedure.

    Returns:
        dict: Message in JSON format
    """
    email = request.json['email']

    if is_email(email) == True:
        api_key = generate_api_key()
        send_apikey_email(email, api_key)
        # Here I need to add some sort of database storing thing
        return jsonify({'message': 'API Ket email sent.')
    else:
        return jsonify({'error':f'{email} is not a valid email'})

if __name__ == '__main__':
    app.run()
