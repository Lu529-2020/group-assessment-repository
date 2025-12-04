"""
Student model definition for the application.

This module defines the `Student` class, representing a student enrolled
in the system. It inherits from `BaseModel` for common fields and includes
attributes for student identification, personal details, and academic
enrollment information.
"""

from datetime import datetime
from .base_model import BaseModel

class Student(BaseModel):
    """
    Represents a student in the system.

    Inherits from `BaseModel` for common fields such as `id`, `created_at`,
    and `is_active`. Students are core entities, linked to various academic
    and wellbeing records.
    """
    def __init__(self, id=None, student_number=None, full_name=None, email=None, course_name=None, year_of_study=None, created_at=None, is_active=True, **kwargs):
        """
        Initializes a Student instance.

        Args:
            id (int, optional): The unique identifier for the student.
            student_number (str, optional): The student's unique identification number (e.g., 'S0001').
            full_name (str, optional): The full name of the student.
            email (str, optional): The primary email address of the student.
            course_name (str, optional): The name of the course or program the student is enrolled in.
            year_of_study (int, optional): The student's current year of study (e.g., 1, 2).
            created_at (datetime, optional): The timestamp when the student record was created. Defaults to current UTC time.
            is_active (bool, optional): Whether the student record is active. Defaults to True.
            **kwargs: Additional keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(id=id, created_at=created_at, is_active=is_active, **kwargs)
        self.student_number = student_number
        self.full_name = full_name
        self.email = email
        self.course_name = course_name
        self.year_of_study = year_of_study

    def to_dict(self) -> dict:
        """
        Converts the Student object to a dictionary representation, including common base model fields.

        Returns:
            dict: A dictionary containing the student's attributes suitable for JSON serialization.
        """
        pass

    @classmethod
    def from_row(cls, row) -> 'Student':
        """
        Creates a Student instance from a database row.

        This class method is used to reconstruct a Student object from data
        retrieved from the database. It leverages `BaseModel.from_row`
        for common fields and then populates student-specific attributes.

        Args:
            row: The database row, expected to be a dict-like object (e.g., `sqlite3.Row`).

        Returns:
            Student: A Student instance populated with data from the row, or None if the row is None.
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the Student object, useful for debugging.
        """
        return f'<Student ID: {self.id}, Name: {self.full_name}, Number: {self.student_number}>'
