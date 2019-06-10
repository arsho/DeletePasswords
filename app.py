# Program              : Search and Delete Saved Password in Chrome Browser
# Author               : Ahmedur Rahman Shovon
# Description          : Search a specific string in saved passwords in Chrome and
#                        deletes all searched passwords
#                        THE ACTIONS CAN NOT BE REVERTED. DO IT IN YOUR OWN RISKS.
# Date                 : 2019/06/10
# Version              : 0.0.1
# Tested OS            : Windows 10
# Python Version       : Python 3.7

import webbrowser
import time
import pyautogui as pt

TAB_KEY = 'tab'
ENTER_KEY = 'enter'
DOWN_KEY = 'down'
BLANK_URL = ""
PASSWORD_URL = "chrome://settings/passwords"

BROWSER_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(BROWSER_PATH))
CHROME = webbrowser.get('chrome')


def open_blank_tab():
    try:
        # Open a blank tab
        CHROME.open(BLANK_URL, new=2)
        # Wait for few seconds to load the blank tab
        time.sleep(2)
        return True
    except Exception as e:
        print("Error occurred while opening the blank tab")
        print(str(e))
    return False

def open_password_page():
    try:
        if open_blank_tab():
            # type the password url
            pt.typewrite(PASSWORD_URL)
            # press enter after typing the search time
            pt.press(ENTER_KEY)
            # Wait for few seconds to load the blank tab
            time.sleep(2)
            return True
    except Exception as e:
        print("Error occurred while opening the password page")
        print(str(e))
    return False

def perform_search(search_term):
    try:
        if open_password_page():
            # press tab 3 times to go to search input
            pt.press([TAB_KEY, TAB_KEY, TAB_KEY])
            # type the search term
            pt.typewrite(search_term)
            # press enter after typing the search time
            pt.press(ENTER_KEY)
            # Wait for few seconds to load the blank tab
            time.sleep(2)
            return True
    except Exception as e:
        print("Error occurred while searching the term")
        print(str(e))
    return False

def search_term_in_saved_passwords(search_term="nfs"):
    try:
        if perform_search(search_term):
            return True
    except Exception as e:
        print("Error occurred while searching the term")
        print(str(e))
    return False

def delete_single_item(first_item = False):
    try:
        tab_press = 3
        if first_item:
            # press tab 8 times to go to item if first_item
            tab_press = 8
        pt.press([TAB_KEY for i in range(tab_press)])
        # press enter after finding the item
        pt.press(ENTER_KEY)
        # press down key two times to select remove button
        pt.press([DOWN_KEY, DOWN_KEY])
        # press enter to delete the item
        pt.press(ENTER_KEY)
        time.sleep(2)
        return True
    except Exception as e:
        print("Error occurred while deleting the saved password")
        print(str(e))
    return False


def search_and_delete():
    searched_finish = search_term_in_saved_passwords()
    first_item = True
    count_item = 0
    try:
        while True:
            if searched_finish:
                if delete_single_item(first_item):
                    count_item += 1
                else:
                    break
                first_item = False
            else:
                print("Can not complete searching the term in saved password.")
    except Exception as ex:
        print("Error occurred")
        print(str(ex))
    return count_item

if __name__ == '__main__':
    deleted_items = search_and_delete()
    print("Number of deleted passwords: {}".format(deleted_items))
