# Utilities

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