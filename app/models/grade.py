"""
Grade model definition for the application.

This module defines the `Grade` class, representing a student's achieved
score or evaluation for a specific assessment within a module. It inherits
from `BaseModel` for common fields and includes attributes for linking
students and modules, assessment name, and the grade value.
"""
from datetime import datetime
from .base_model import BaseModel


class Grade(BaseModel):
    """
    Represents a grade for a student's assessment in a module.

    Inherits from `BaseModel` for common fields such as `id`, `created_at`,
    and `is_active`. Grades are linked to a specific student, module, and assessment.
    """

    def __init__(self, id=None, student_id=None, module_id=None, assessment_name=None, grade=None, student_name=None,
                 module_title=None, created_at=None, is_active=True, **kwargs):
        """
        Initializes a Grade instance.

        Args:
            id (int, optional): The unique identifier for the grade record.
            student_id (int, optional): The ID of the student who received this grade.
            module_id (int, optional): The ID of the module for which this grade was given.
            assessment_name (str, optional): The name or description of the assessment (e.g., 'Midterm', 'Final Project').
            grade (float, optional): The numerical grade value.
            student_name (str, optional): The full name of the student (often populated via JOINs).
            module_title (str, optional): The title of the module (often populated via JOINs).
            created_at (datetime, optional): The timestamp when the record was created. Defaults to current UTC time.
            is_active (bool, optional): Whether the record is active. Defaults to True.
            **kwargs: Additional keyword arguments passed to the BaseModel constructor.
        """
        super().__init__(id=id, created_at=created_at, is_active=is_active, **kwargs)
        self.student_id = student_id
        self.module_id = module_id
        self.assessment_name = assessment_name
        self.grade = grade
        self.student_name = student_name
        self.module_title = module_title

    def to_dict(self) -> dict:
        """
        Converts the Grade object to a dictionary representation, including common base model fields.

        Returns:
            dict: A dictionary containing the grade's attributes suitable for JSON serialization.
        """
        pass

    @classmethod
    def from_row(cls, row) -> 'Grade':
        """
        Creates a Grade instance from a database row.

        This class method is used to reconstruct a Grade object from data
        retrieved from the database. It leverages `BaseModel.from_row`
        for common fields and then populates grade-specific attributes.

        Args:
            row: The database row, expected to be a dict-like object (e.g., `sqlite3.Row`).

        Returns:
            Grade: A Grade instance populated with data from the row, or None if the row is None.
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the Grade object, useful for debugging.
        """
        return f'<Grade ID: {self.id}, Student: {self.student_id}, Assessment: "{self.assessment_name}">'

