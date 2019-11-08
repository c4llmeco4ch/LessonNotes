import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import date
import sys
'''import typing
from typing import TypeVar

DT = TypeVar('DT', date)'''

def printLessons(day = datetime.today(), displayNotes = False):
    """
    For a given day, print out the names of the students
    If 'displayNotes' is true, also show the past lesson's note
    """
    url = 'https://tcs-sanramon.pike13.com/today'
    url += ('#/list?dt={year}-{month}-{day}').format(year=day.year, month=day.month, day=day.day)
    


def addNotes(student, day = datetime.today()):
    """Take in user inputs to send notes for a given student"""
    pass


def determineBasePath() -> str:
    if sys.platform == "linux" or sys.platform == "linux2":
        return r'/usr/lib/firefox/firefox'
    elif "win" in sys.platform.lower():
        return r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    elif sys.platform == "darwin":
        return r'/Applications/Firefox.app'


def checkLogin():
    """
    Check that the user is logged in
    If not, log in using provided credentials
    Or prompt the user for credentials
    """
    pass


if __name__ == "__main__":
    ffPath = determineBasePath()
    ffLoc = FirefoxBinary(ffPath)
    browser = webdriver.Firefox(firefox_binary=ffLoc)
    checkLogin()
