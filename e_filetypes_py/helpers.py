import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
import json

def generate_key(passkey: str, salt: bytes, iterations: int = 100000) -> bytes:
    """
    Generates a key from a passkey and salt. The key is used to encrypt and decrypt files.

    Args:
        passkey (str): Passkey used to generate the key
        salt (str): Salt used to generate the key

    Returns:
        bytes: Key used to encrypt and decrypt files
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    return kdf.derive(passkey.encode())

def encrypt_data(data: bytes, passkey: str) -> bytes:
    """
    Encrypts data using AES-GCM, which is good for encrypting large amounts of data.

    Args:
        data (bytes): Data to be encrypted
        key (bytes): Key used to encrypt the data

    Returns:
        bytes: Encrypted data
    """
    salt = os.urandom(16)
    key = generate_key(passkey, salt)
    aesgcm = AESGCM(key) 
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)

    encrypted_data = base64.b64encode(salt + nonce + ciphertext)
    return encrypted_data

def write_file_header(path: str, passkey: str, metadata: dict = {}) -> None:
    """
    Writes the file header of an encrypted file. The first 256 bytes of the file are reserved for the file header. Writes 'e-*' as a way to distinguish the file and then encrypts any metadata into the file header.

    Args:
        path (str): Path to the encrypted file
        metadata (dict): Metadata to be encrypted into the file header. Defaults to an empty dictionary. Common metadata includes the name of the file, the author, the date, and a description.
        passkey (str): Passkey used to encrypt the file header. Must be the same passkey used to encrypt the file.

    Raises:
        FileNotFoundError: If the file does not exist
        Exception: The process failed for an unknown reason
    """

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File '{path}' does not exist. Is there a typo?")
    try:
        with open(path, 'rb+') as f:
            f.seek(0)
            f.write(b'e-*')
            metadata_json = json.dumps(metadata)
            encrypted_metadata = encrypt_data(metadata_json.encode(), passkey)
            f.write(encrypted_metadata.ljust(256, b'\0'))
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' does not exist. Is there a typo?")
    except Exception:
        raise Exception(f"Failed to write file header for '{path}'.")

def read_file_header(path: str, passkey: str) -> dict:
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
        Exception: The process failed for an unknown reason

    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File '{path}' does not exist. Is there a typo?")
    try:
        with open(path, 'rb') as f:
            file_header = f.read(3)
            if file_header != b'e-*':
                raise ValueError(f"File '{path}' is not encrypted. Please use encrypt the file to an EType first.")
            f.seek(3)
            header_bytes = f.read(256) # e-* must have a header of 256 bytes
            header_encrypted = base64.b64decode(header_bytes.rstrip(b'\0').decode('utf-8'))
            salt = header_encrypted[:16]
            nonce = header_encrypted[16:28]
            ciphertext = header_encrypted[28:]
            key = generate_key(passkey, salt)
            aesgcm = AESGCM(key)
            try:
                header_json = json.loads(aesgcm.decrypt(nonce, ciphertext, None))
                return header_json
            except ValueError:
                raise ValueError(f"Incorrect passkey for '{path}'.")
            except Exception:
                raise Exception(f"Failed to read file header for '{path}'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' does not exist. Is there a typo?")
    except json.decoder.JSONDecodeError:
        raise ValueError(f"File '{path}' is not encrypted. Please use encrypt the file to an EType first.")
    except UnicodeDecodeError:
        raise ValueError(f"File '{path}' is not encrypted. Please use encrypt the file to an EType first.")
    except Exception:
        raise ValueError(f"File '{path}' is not encrypted. Please use encrypt the file to an EType first.")
