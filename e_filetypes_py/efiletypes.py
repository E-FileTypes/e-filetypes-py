import os
from helpers import read_file_header

def get_file_header(path: str, passkey: str) -> dict:
    """
    Reads the file header of an encrypted file and returns the file header.

    Args:
        path (str): Path to the encrypted file
        passkey (str): Passkey used to encrypt the file header. Must be the same passkey used to encrypt the file.

    Returns:
        dict: File header   

    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is not encrypted     
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File '{path}' does not exist. Is there a typo?")
    try:
        return read_file_header(path, passkey)
    except ValueError:
        raise ValueError(f"File '{path}' is not encrypted. Please use encrypt the file to an EType first.")
    except Exception:
        raise Exception(f"Failed to read file header for '{path}'.")
    

print(get_file_header('test.txt', 'test'))

