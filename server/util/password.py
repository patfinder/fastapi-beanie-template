"""Password utility functions."""

import bcrypt

from server.config import CONFIG


def hash_password(password: str) -> str:
    """Return a salted password hash."""
    return bcrypt.hashpw(password.encode(), CONFIG.salt).decode()
