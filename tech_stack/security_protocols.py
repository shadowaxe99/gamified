```python
import os
from cryptography.fernet import Fernet

# Define a class to handle security protocols, particularly data encryption and decryption
class SecurityProtocols:
    def __init__(self):
        # Generate a key for encryption and decryption
        # In a real-world scenario, this key should be securely stored and managed
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)

    def encrypt_data(self, data):
        """
        Encrypts the provided data using Fernet symmetric encryption.
        
        :param data: Data to be encrypted (bytes).
        :return: Encrypted data (bytes).
        """
        if isinstance(data, str):
            data = data.encode()  # Ensure the data is in bytes
        encrypted_data = self.cipher_suite.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the provided data using Fernet symmetric encryption.
        
        :param encrypted_data: Data to be decrypted (bytes).
        :return: Decrypted data (bytes).
        """
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data

    def save_encryption_key(self, file_path):
        """
        Saves the encryption key to a file.
        
        :param file_path: Path to the file where the key will be saved.
        """
        with open(file_path, 'wb') as key_file:
            key_file.write(self.encryption_key)

    def load_encryption_key(self, file_path):
        """
        Loads the encryption key from a file.
        
        :param file_path: Path to the file where the key is stored.
        """
        with open(file_path, 'rb') as key_file:
            self.encryption_key = key_file.read()
            self.cipher_suite = Fernet(self.encryption_key)

# Example usage:
# security = SecurityProtocols()
# encrypted_data = security.encrypt_data('Sensitive data')
# decrypted_data = security.decrypt_data(encrypted_data)
# security.save_encryption_key('path/to/keyfile.key')
# security.load_encryption_key('path/to/keyfile.key')
```