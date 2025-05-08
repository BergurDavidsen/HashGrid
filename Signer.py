from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import base64
import json


class Signer:
    def __init__(self, private_key=None):
        self.private_key = private_key or self.generate_key()
        self.public_key = self.private_key.public_key()

    def generate_key(self):
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

    def sign(self, message: str) -> str:
        signature = self.private_key.sign(
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()

    def get_public_key_pem(self) -> str:
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode()

    def export_private_key(self) -> str:
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        return pem.decode()

    @staticmethod
    def verify_signature(message: str, signature_b64: str, public_key_pem: str) -> bool:
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        signature = base64.b64decode(signature_b64.encode())
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
