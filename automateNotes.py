import selenium, sys, getopt  #, typing
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import date
'''
from typing import TypeVar
DT = TypeVar('DT', date)
'''

OPTIONS = 'd:pna:'
LONG_OPTIONS = ['day=', 'print', 'notes', 'add=']
ffPath = determineBasePath()
ffLoc = FirefoxBinary(ffPath)
browser = webdriver.Firefox(firefox_binary=ffLoc)

def printLessons(driver = browser, day = datetime.today(), displayNotes = False):
    """
    For a given day, print out the names of the students
    If 'displayNotes' is true, also show the past lesson's note
    """
    pass


def checkLogin(driver = browser, day = datetime.today()):
    """
    Check that the user is logged in
    If not, log in using provided credentials
    Or prompt the user for credentials
    """
    url = 'https://tcs-sanramon.pike13.com/today'
    url += ('#/list?dt={year}-{month}-{day}').format(year=day.year, month=day.month, day=day.day)
    driver.get(url)
    if 'sign_in' in driver.current_url:
        pass
    


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


def printHelp():
    """The help message for using this module"""
    print('Options: '
          + '-d or --day: Assumed today, the day in yyyy/mm/dd format\n'
          + '-p or --print: Print the lessons for the day\n'
          + '-n or --notes: Print the last note for each student\n'
          + '-a or --add: Add notes for the provided student')


def main(args):
    optArgs, regArgs = getopt.getopt(args, OPTIONS, LONG_OPTIONS)
    checkLogin()


if __name__ == "__main__":
    main(sys.argv[1:])
