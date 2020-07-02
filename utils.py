# Utilities

import re


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
