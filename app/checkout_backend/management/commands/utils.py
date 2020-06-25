import os


def get_full_path(filename):
    """Returns the full path of the filename inside commands folder"""

    return os.path.join(os.path.dirname(__file__), filename)
