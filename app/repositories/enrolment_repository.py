"""
Enrolment Repository module for managing student enrolment data.

This module defines the `EnrolmentRepository` class, which provides methods
for interacting with the 'enrolments' table in the database. It extends
`BaseRepository` to handle CRUD operations for enrolments, including
retrieving records with joined student and module information.
"""

import sqlite3
from app.db_connection import get_db
from app.models.enrolment import Enrolment
from datetime import datetime, timezone
from .base_repository import BaseRepository

class EnrolmentRepository(BaseRepository):
    """
    Repository for enrolment-related database operations.

    Inherits from `BaseRepository` to leverage common CRUD functionality
    and error handling. Provides specific methods for querying and managing
    student enrolments.
    """
    def __init__(self):
        """
        Initializes the EnrolmentRepository.

        Sets the table name to 'enrolments' and the model class to `Enrolment`.
        """
        super().__init__('enrolments', Enrolment)

    def get_all_enrolments(self) -> list[dict]:
        """
        Retrieves all active enrolments from the database, including associated
        student and module information for richer context.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary represents
                        an enrolment with joined student and module details.
        """
        pass

    def get_enrolment_by_id(self, enrolment_id: int) -> Enrolment | None:
        """
        Retrieves a single enrolment by its unique ID.

        Args:
            enrolment_id (int): The unique identifier of the enrolment to retrieve.

        Returns:
            Enrolment | None: An `Enrolment` object if found, otherwise None.
        """
        pass

    def create_enrolment(self, student_id: int, module_id: int, enrol_date: str | None = None) -> Enrolment:
        """
        Creates a new enrolment record in the database.

        Args:
            student_id (int): The ID of the student to enroll.
            module_id (int): The ID of the module to enroll in.
            enrol_date (str, optional): The enrolment date in ISO format. Defaults to the current UTC date.

        Returns:
            Enrolment: The newly created `Enrolment` object.
        """
        pass

    def update_enrolment(self, enrolment_id: int, student_id: int, module_id: int, enrol_date: str) -> Enrolment:
        """
        Updates an existing enrolment record in the database.

        Args:
            enrolment_id (int): The unique identifier of the enrolment to update.
            student_id (int): The new student ID for the enrolment.
            module_id (int): The new module ID for the enrolment.
            enrol_date (str): The new enrolment date in ISO format.

        Returns:
            Enrolment: The updated `Enrolment` object.
        """
        pass

    def delete_enrolment(self, enrolment_id: int) -> bool:
        """
        Logically deletes an enrolment by setting its 'is_active' flag to 0.

        Args:
            enrolment_id (int): The unique identifier of the enrolment to logically delete.

        Returns:
            bool: True if the enrolment was successfully logically deleted, False otherwise.
        """
        pass

# Instantiate the repository for use throughout the application.
enrolment_repository = EnrolmentRepository()
