import os
import inspect


def get_caller_file_path(filename: str) -> str:
    """
    Get the full path to a file in the directory of the calling script.

    Args:
        filename (str): The name of the file to resolve.

    Returns:
        str: The full path to the file.
    """
    # Get the stack frame of the caller
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(caller_file)
    return os.path.join(caller_dir, filename)
