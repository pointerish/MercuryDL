import json
import hashlib
import shlex, subprocess
from utils import is_safe

class YTDLSession:

    """
    This class contains the YoutubeDL methods needed to download the files.
    """

    def __init__(self, params : str, api_token : str) -> None:
        self.params = params
        self.api_token = api_token
        self.ses_token = hashlib.sha256(str.encode(self.api_token)).hexdigest()

    def __str__(self) -> str:
        return f'YTDLSession("{self.params}", "{self.api_token}") with Session ID <{self.ses_token}>'

    def _download(self) -> dict:
        download_args = shlex.split(self.params)
        if is_safe(download_args) == True:
            execution = subprocess.check_output(download_args) # Need to make sure this is safe!
            file_name = execution.decode('utf-8').split('[ffmpeg] Destination: ')[1].split('\n')[0]
            return {'msg':'Success!', 'file':file_name}
        else:
            return {'msg':'Non Youtube-DL \
                     command/option not allowed. \
                     Use a valid Youtube-DL command/option.',
                     'file':'null'}

    def _store_session(self) -> None:
        with open('sessions.json', 'w') as sessions:
            json.dump({self.ses_token:hashlib.sha256(str.encode(self.params)).hexdigest()}, sessions)