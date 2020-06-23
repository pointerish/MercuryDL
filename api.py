from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file
from mercury_dl import YTDLSession

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    args = request.json['args']
    user = request.json['user']
    session = YTDLSession(args, user)
    execution = session._download()
    if execution['msg'] == 'Success!':
        return send_file(f'./{execution["file"]}', attachment_filename=execution['file'])
    else:
        return jsonify({'status':execution['msg']})

if __name__ == '__main__':
    app.run()
