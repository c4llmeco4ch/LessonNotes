import selenium
from selenium import webdriver
from datetime import date
import typing
from typing import TypeVar

DT = TypeVar('DT', date)

def printLessons(date: datetime, displayNotes = False: bool) -> None:
    """
    For a given day, print out the names of the students
    If 'displayNotes' is true, also show the past lesson's note
    """
    pass

def addNotes(student: str, date = today: datetime) -> bool:
    """Take in user inputs to send notes for a given student"""
    pass