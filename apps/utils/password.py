from cryptography.fernet import Fernet

from apps.utils.main import config

SECRET_KEY = config.SECRET_KEY

def hash_password(password: str) -> str:
    return Fernet(SECRET_KEY).encrypt(password.encode()).decode()

