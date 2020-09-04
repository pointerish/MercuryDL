# Utilities

import os
import re
import uuid
import yagmail


def is_safe(args: list) -> bool:
    """This function returns True if the arguments are allowed.
       Returns False if there are arguments that are not allowed.

    Args:
        args (list): command-line arguments

    Returns:
        bool: True or False
    """
    valid_options = ['youtube-dl', '-x', '--audio-format', 'mp3']
    checkups = []

    for arg in args:
        if arg in valid_options or 'https://www.youtube.com/' in arg:
            checkups.append(True)
        else:
            checkups.append(False)

    if False not in checkups:
        return True
    else:
        return False


def is_email(email : str) -> bool:
    """This function checks whether the email provided is a valid email.

    Args:
        email (str): An email address

    Returns:
        bool
    """
    email_pattern = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    email_match   = email_pattern.match(email)
    if email_match != None:
        return True
    else:
        return False

def generate_api_key() -> str:
    """
    This function generates the API key using the uuid module
    """
    return uuid.uuid4().hex

def send_apikey_email(email: str, api_key: str) -> None:
    """This function sends an email containing the API Key for the user"""
    # The email and password are stored as environment variables and added to yagmail
    # using os.environ.
    # I am temporarily using Gmail SMTP but here we could potentially use SendGrid or
    # some other email sender API.
    yag = yagmail.SMTP(user=os.environ['MERCURY_EMAIL'], password=os.environ['MERCURY_PSSWD'])
    yag.send(to=email, subject='MercuryDL API Key', contents=api_key)