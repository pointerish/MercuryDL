import hashlib
import youtube_dl
import shlex, subprocess

class YTDLSession:

    def __init__(self, params, session_user):
        self.params = params
        self.session_user = session_user
        self.session_id = hashlib.sha256(str.encode(session_user)).hexdigest()

    def __str__(self):
        return f'YTDLSession("{self.params}", "{self.session_user}") with Session ID <{self.session_id}>'

    def _download(self):
        download_args = shlex.split(self.params)
        if download_args[0] == 'youtube-dl':
            execution = subprocess.check_output(download_args) # Need to make sure this is safe!
            file_name = execution.decode('utf-8').split('[ffmpeg] Destination: ')[1].split('\n')[0]
            return {'msg':'Success!', 'file':file_name}
        else:
            return {'msg':'Non Youtube-DL command not allowed. Use a valid Youtube-DL command.'}
