import selenium, sys, getopt  #, typing
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, time

'''
from typing import TypeVar
DT = TypeVar('DT', date)
'''


def determineBasePath() -> str:
    if sys.platform == "linux" or sys.platform == "linux2":
        return r'/usr/lib/firefox/firefox'
    elif "win" in sys.platform.lower():
        return r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    elif sys.platform == "darwin":
        return r'/Applications/Firefox.app'


OPTIONS = 'hd:pna:'
LONG_OPTIONS = ['day=', 'print', 'notes', 'add=']
ffOpts = Options()
ffOpts.headless = False
ffPath = determineBasePath()
ffLoc = FirefoxBinary(ffPath)
browser = webdriver.Firefox(firefox_binary=ffLoc, options=ffOpts)


def timer(tag, value, length, driver=browser):
    timeout = length
    if tag == 'id':
        loc = (By.ID, value)
    elif tag == 'class':
        loc = (By.CLASS_NAME, value)
    elif tag == 'xpath':
        loc = (By.XPATH, value)
    elif tag == 'tag_name':
        loc = (By.TAG_NAME, value)
    try:
        foundElement = EC.presence_of_element_located(loc)
        WebDriverWait(driver, timeout).until(foundElement)
    except TimeoutException:
        print('Couldn\'t find {val} in {dur} seconds.'.format(val=value, dur=timeout))
        driver.quit()
        sys.exit()
    else:
        return


def printLessons(driver = browser, day = date.today(), displayNotes = False):
    """
    For a given day, print out the names of the students
    If 'displayNotes' is true, also show the past lesson's note
    """
    timer('id', 'schedule-list', 10)
    lessonTable = driver.find_element_by_id('schedule-list')
    timePassed = 0
    while 'Loading' in lessonTable.text:
        if timePassed % 600 < 1:
            print('Loading...')
    for lesson in lessonTable.find_elements_by_tag_name('tr'):
        student = lesson.find_element_by_css_selector('strong.ng-binding')
        time = [lesson.find_element_by_xpath('//*[@id="schedule-list"]/tbody/tr[2]/td[1]/span[1]'),
                lesson.find_element_by_xpath('//*[@id="schedule-list"]/tbody/tr[2]/td[1]/span[2]')]
        print(len(student))  # TODO: Figure out why we can't find student names
        print('|{start} - {end}: {name}|'.format(start=time[0].text,
                                                 end=time[1].text,name=student.text))


def checkLogin(driver = browser, day = date.today()) -> bool:
    """
    Check that the user is logged in
    If not, log in using provided credentials
    Or prompt the user for credentials
    """
    url = 'https://tcs-sanramon.pike13.com/today'
    url += ('#/list?dt={year}-{month}-{day}').format(year=day.year, month=day.month, day=day.day)
    driver.get(url)
    print('sign_in' in driver.current_url)
    return 'sign_in' in driver.current_url


def completeLogin(driver = browser):
    """Log in to Pike13 using the provided credentials"""
    credentials = []
    with open('credentials.txt') as login:
        credentials = login.read().split(':')
    timer('id', 'account_email', 5)
    driver.find_element_by_id('account_email').send_keys(credentials[0])
    driver.find_element_by_id('account_password').send_keys(credentials[1] + Keys.RETURN)


def addNotes(student, day = date.today()):
    """Take in user inputs to send notes for a given student"""
    pass


def printHelp():
    """The help message for using this module"""
    print('Options:\n'
          + '-h: Display this message'
          + '-d or --day: Assumed today, the day in "yyyy-mm-dd" format\n'
          + '-p or --print: Print the lessons for the day\n'
          + '-n or --notes: Print the last note for each student\n'
          + '-a or --add: Add notes for the provided student')


def main(args):
    options, _ = getopt.getopt(args, OPTIONS, LONG_OPTIONS)
    day = date.today()
    arePrinting = False
    areSubmitting = False
    student = None
    for opt, arg in options:
        if opt == '-h':
            printHelp()
            browser.quit()
            sys.exit()
        elif opt in ('-d', '--day'):
            day = arg.split('-')
        elif opt in ('-p', '--print'):
            arePrinting = True
        elif opt in ('-n', '--notes'):
            areSubmitting = True
        elif opt in ('-a', '--add'):
            student = arg
    if areSubmitting and student is None:
        print('Must include a student to submit notes.\n'
              + 'Use \'-a\' or \'--add\'')
        sys.exit()
    if checkLogin():
        completeLogin()
    if arePrinting:
        printLessons(day=day)
    if areSubmitting:
        addNotes(student,day=day)
    browser.quit()


if __name__ == "__main__":
    main(sys.argv[1:])
