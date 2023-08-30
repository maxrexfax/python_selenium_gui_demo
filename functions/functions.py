from datetime import datetime
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# import reportHelper as rp


def create_log_file():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    directory = "logs"

    if not os.path.exists(directory):
        os.mkdir(directory)

    file_name = directory + "/" + now + "_logs.txt"
    try:
        logfile = open(file_name, "w")
        try:
            logfile.write("Log started at:" + now + "\n")
        except Exception as e:
            print(e)
        finally:
            logfile.close()
    except Exception as ex:
        print(ex)
    return file_name


def add_line_to_log_and_print_msg(filename, message):
    print(message)
    try:
        logfile = open(filename, "a")
        try:
            logfile.write(message + "\n")
        except Exception as e:
            print(e)
        finally:
            logfile.close()
    except Exception as ex:
        print(ex)


def mark_widget_as_deleted(list_of_widgets, header_deleted_text):
    for widget_to_mark in list_of_widgets:
        if widget_to_mark.header == header_deleted_text:
            widget_to_mark.is_removed = True


def find_element_dynamic_timeout(parent, type_of_selector, selector, max_time):
    max_time -= 1
    result = None
    if max_time > 0:
        try:
            if type_of_selector == "XPATH":
                result = parent.find_element(By.XPATH, selector)
            elif type_of_selector == "CLASS_NAME":
                result = parent.find_element(By.CLASS_NAME, selector)
            elif type_of_selector == "CSS_SELECTOR":
                result = parent.find_element(By.CSS_SELECTOR, selector)
            elif type_of_selector == "ID":
                result = parent.find_element(By.ID, selector)
            elif type_of_selector == "NAME":
                result = parent.find_element(By.NAME, selector)
            elif type_of_selector == "LINK_TEXT":
                result = parent.find_element(By.LINK_TEXT, selector)
            elif type_of_selector == "PARTIAL_LINK_TEXT":
                result = parent.find_element(By.PARTIAL_LINK_TEXT, selector)
            elif type_of_selector == "TAG_NAME":
                result = parent.find_element(By.TAG_NAME, selector)

            return result
        except NoSuchElementException:
            if max_time > 0:
                find_element_dynamic_timeout(parent, type_of_selector, selector, max_time)
            else:
                return None
    else:
        return None

