"""
Student Repository module for managing student data.

This module defines the `StudentRepository` class, which provides methods
for interacting with the 'students' table in the database. It extends
`BaseRepository` to handle CRUD operations for students, including
retrieving student details and their associated enrolments.
"""

import sqlite3
from app.db_connection import get_db
from app.models.student import Student
from .base_repository import BaseRepository
from flask import current_app # Import current_app for logging

class StudentRepository(BaseRepository):
    """
    Repository for student-related database operations.

    Inherits from `BaseRepository` to leverage common CRUD functionality
    and error handling. Provides specific methods for querying and managing
    student records.
    """
    def __init__(self):
        """
        Initializes the StudentRepository.

        Sets the table name to 'students' and the model class to `Student`.
        """
        super().__init__('students', Student)

    def get_all_students(self, include_inactive: bool = False) -> list[Student]:
        """
        Retrieves all active students from the database.

        Args:
            include_inactive (bool, optional): If True, includes students marked as inactive. Defaults to False.

        Returns:
            list[Student]: A list of `Student` objects representing all active (or all) students.
        """
        pass

    def get_student_by_id(self, student_id: int, include_inactive: bool = False) -> Student | None:
        """
        Retrieves a single student by their unique ID.

        Args:
            student_id (int): The unique identifier of the student to retrieve.
            include_inactive (bool, optional): If True, includes inactive students. Defaults to False.

        Returns:
            Student | None: A `Student` object if found, otherwise None.
        """
        pass

    def get_student_by_student_number(self, student_number: str) -> Student | None:
        """
        Retrieves a single student by their unique student number.

        Args:
            student_number (str): The student number to search for.

        Returns:
            Student | None: A `Student` object if found, otherwise None.
        """
        pass
    def get_student_enrolments(self, student_id: int) -> list[dict]:
        """
        Retrieves all active enrolments for a specific student, including module details.

        Args:
            student_id (int): The unique identifier of the student.

        Returns:
            list[dict]: A list of dictionaries, each representing an enrolment
                        with associated module code and title.
        """
        pass

    def create_student(self, student_number: str, full_name: str, email: str, course_name: str | None, year_of_study: int | None) -> Student:
        """
        Creates a new student record in the database.

        Args:
            student_number (str): The unique student number.
            full_name (str): The full name of the student.
            email (str): The email address of the student.
            course_name (str | None): The name of the course the student is enrolled in.
            year_of_study (int | None): The student's current year of study.

        Returns:
            Student: The newly created `Student` object.
        """
        pass

    def update_student(self, student_id: int, student_number: str, full_name: str, email: str, course_name: str | None, year_of_study: int | None) -> Student:
        """
        Updates an existing student's information in the database.

        Args:
            student_id (int): The unique identifier of the student to update.
            student_number (str): The new unique student number.
            full_name (str): The new full name of the student.
            email (str): The new email address of the student.
            course_name (str | None): The new course name.
            year_of_study (int | None): The new year of study.

        Returns:
            Student: The updated `Student` object.
        """
        pass

    def delete_student(self, student_id: int) -> bool:
        """
        Logically deletes a student by setting their 'is_active' flag to 0.

        Args:
            student_id (int): The unique identifier of the student to logically delete.

        Returns:
            bool: True if the student was successfully logically deleted, False otherwise.
        """
        pass

    def delete_student_hard(self, student_id: int) -> bool:
        """
        Permanently deletes a student record from the database.

        Use this method with caution, as data deleted this way cannot be recovered.

        Args:
            student_id (int): The unique identifier of the student to permanently delete.

        Returns:
            bool: True if the student was successfully permanently deleted, False otherwise.
        """
        pass

# Instantiate the repository for use throughout the application.
student_repository = StudentRepository()
