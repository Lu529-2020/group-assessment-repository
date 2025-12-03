"""
Base model definition for the application.

This module defines the `BaseModel` class, which provides common attributes
and methods (like ID, active status, creation timestamp, and dictionary conversion)
for all other data models in the application. It also includes a class method
to instantiate a model from a database row, handling common data parsing.
"""

from datetime import datetime, timezone
from flask import current_app # Imported here for logging within from_row, if app context is available

class BaseModel:
    """
    A base model class providing common fields and methods for all other models.

    Attributes:
        id (int): The unique identifier for the record.
        is_active (bool): Indicates whether the record is active (True) or logically deleted (False).
        created_at (datetime): The UTC timestamp when the record was created.
    """
    def __init__(self, id=None, is_active=True, created_at=None):
        """
        Initializes a new instance of the BaseModel.

        Args:
            id (int, optional): The unique identifier for the record. Defaults to None (for new records).
            is_active (bool, optional): The active status of the record. Defaults to True.
            created_at (datetime, optional): The creation timestamp. Defaults to the current UTC time if None.
        """
        self.id = id
        self.is_active = is_active
        # Set created_at to current UTC time if not provided.
        self.created_at = created_at if created_at is not None else datetime.now(timezone.utc)

    def to_dict(self):
        """
        Converts the common fields of the model instance to a dictionary representation.

        This method is designed to be extended by subclasses to include their
        specific attributes.

        Returns:
            dict: A dictionary containing the common attributes (id, is_active, created_at).
        """
        pass

    @classmethod
    def from_row(cls, row):
        """
        Creates a BaseModel instance (or a subclass instance) from a database row.

        This class method is intended to be called by subclasses' `from_row`
        implementations to handle the parsing of common fields.

        Args:
            row: The database row, expected to be a dict-like object (e.g., `sqlite3.Row`).

        Returns:
            BaseModel: A BaseModel instance (or an instance of the calling subclass)
                       populated with common fields, or None if the input row is None.
        """
        pass
