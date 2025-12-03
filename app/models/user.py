"""
User model definition for the application.

This module defines the `User` class, representing a user of the system
with attributes like username, password hash, role, and an optional link
to a student record. It inherits from `BaseModel` for common fields and
provides methods for password management.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .base_model import BaseModel

class User(BaseModel):
    """
    Represents a user of the system.

    Inherits from `BaseModel` for common fields such as `id`, `created_at`,
    and `is_active`. Includes specific attributes for user authentication
    and role management.
    """
    def __init__(self, id=None, username=None, password_hash=None, role='user', student_id=None, created_at=None, is_active=True, **kwargs):
        """
        Initializes a User instance.

        Args:
            id (int, optional): The unique identifier for the user.
            username (str, optional): The user's unique username.
            password_hash (str, optional): The hashed password for the user.
            role (str, optional): The role of the user (e.g., 'admin', 'student', 'course_director', 'wellbeing_officer'). Defaults to 'user'.
            student_id (int, optional): The ID of the associated student record, if this user is a student. Defaults to None.
            created_at (datetime, optional): The timestamp when the user record was created. Defaults to current UTC time.
            is_active (bool, optional): Whether the user account is active. Defaults to True.
            **kwargs: Additional keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(id=id, created_at=created_at, is_active=is_active, **kwargs)
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.student_id = student_id

    def set_password(self, password: str):
        """
        Hashes the provided plain-text password using Werkzeug's security functions
        and sets it as the user's `password_hash`.

        Args:
            password (str): The plain-text password to hash.
        """
        pass

    def check_password(self, password: str) -> bool:
        """
        Checks if the provided plain-text password matches the user's stored hashed password.

        Args:
            password (str): The plain-text password to check against the stored hash.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        pass

    def to_dict(self) -> dict:
        """
        Converts the User object to a dictionary representation, including common base model fields.

        Returns:
            dict: A dictionary containing the user's attributes suitable for JSON serialization.
        """
        pass

    @classmethod
    def from_row(cls, row) -> 'User':
        """
        Creates a User instance from a database row.

        This class method is used to reconstruct a User object from data
        retrieved from the database. It leverages `BaseModel.from_row`
        for common fields and then populates user-specific attributes.

        Args:
            row: The database row, expected to be a dict-like object (e.g., `sqlite3.Row`).

        Returns:
            User: A User instance populated with data from the row, or None if the row is None.
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the User object, useful for debugging.
        """
        return f'<User {self.username} (ID: {self.id})>'
