"""
Alert Repository module for managing alert-related data.

This module defines the `AlertRepository` class, which provides methods
for interacting with the 'alerts' table in the database. It extends
`BaseRepository` to handle CRUD operations for alerts, including
retrieving specific alerts, marking them as resolved, and creating new ones.
"""

import sqlite3
from app.db_connection import get_db
from app.models.alert import Alert
from .base_repository import BaseRepository

class AlertRepository(BaseRepository):
    """
    Repository for alert-related database operations.

    Inherits from `BaseRepository` to leverage common CRUD functionality
    and error handling. Provides specific methods for querying and managing
    student alerts, often joining with student and module information.
    """
    def __init__(self):
        """
        Initializes the AlertRepository.

        Sets the table name to 'alerts' and the model class to `Alert`.
        """
        super().__init__('alerts', Alert)

    def get_all_alerts(self) -> list[dict]:
        """
        Retrieves all active alerts from the database, including associated
        student and module information for richer context.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary represents
                        an alert with joined student and module details.
        """
        pass

    def get_recent_alerts_per_student(self) -> list[dict]:
        """
        Retrieves the most recent active alert for each student.

        This query identifies the latest alert (by week number) for every student
        and fetches its details along with student and module information.

        Returns:
            list[dict]: A list of dictionaries, each representing the latest
                        active alert for a distinct student.
        """
        pass

    def get_alerts_by_student_id(self, student_id: int) -> list[dict]:
        """
        Retrieves all active alerts for a specific student.

        Args:
            student_id (int): The unique identifier of the student.

        Returns:
            list[dict]: A list of dictionaries, each representing an active alert
                        associated with the given student, including joined details.
        """
        pass

    def get_alert_by_id(self, alert_id: int) -> Alert | None:
        """
        Retrieves a single alert by its unique ID.

        Args:
            alert_id (int): The unique identifier of the alert to retrieve.

        Returns:
            Alert | None: An `Alert` object if found, otherwise None.
        """
        pass

    def mark_alert_resolved(self, alert_id: int) -> bool:
        """
        Marks a specific alert as resolved in the database.

        Args:
            alert_id (int): The unique identifier of the alert to mark as resolved.

        Returns:
            bool: True if the alert was successfully marked as resolved (i.e., a record was updated), False otherwise.
        """
        pass
    
    def delete_alert(self, alert_id: int) -> bool:
        """
        Logically deletes an alert by setting its 'is_active' flag to 0.

        Args:
            alert_id (int): The unique identifier of the alert to logically delete.

        Returns:
            bool: True if the alert was successfully logically deleted, False otherwise.
        """
        pass    

    def create_alert(self, student_id: int, module_id: int | None, week_number: int, reason: str) -> Alert:
        """
        Creates a new alert record in the database.

        Args:
            student_id (int): The ID of the student to whom the alert pertains.
            module_id (int | None): The ID of the module related to the alert (can be None).
            week_number (int): The week number when the alert was generated.
            reason (str): The descriptive reason for the alert.

        Returns:
            Alert: The newly created `Alert` object.
        """
        pass

# Instantiate the repository for use throughout the application.
alert_repository = AlertRepository()