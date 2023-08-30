import os
# import shutil
from datetime import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

marker_header = "<p id='MARKER__HEADER' style='display:none'></p>"
marker_content = ""
header_counter = 0


def create_report_file():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists("report/report.html"):
        os.rename("report/report.html", "report/old/report_moved_at_" + now + ".html")
        # os.remove("report/report.html")
    with open("templates/prereport.html") as f_old, open("report/report.html", "w") as f_new:
        for line in f_old:
            f_new.write(line)
            if '<body>' in line:
                f_new.write('<div style="text-align:right; font-size:2em; color:gray;">Test started at ' + str(now) + '</div>')
            if '<div class="main-container">' in line:
                f_new.write(marker_header)


def write_string_to_report_file(message):
    global marker_content
    fin = open("report/report.html", "rt")
    data = fin.read()
    data = data.replace(marker_content, message + "\n" + marker_content)
    fin.close()
    fin = open("report/report.html", "wt")
    fin.write(data)
    fin.close()


def delete_old_marker_content(marker_to_delete):
    fin = open("report/report.html", "rt")
    data = fin.read()
    data = data.replace(marker_to_delete, "")
    fin.close()
    fin = open("report/report.html", "wt")
    fin.write(data)
    fin.close()


def write_header(header):
    global marker_header
    global marker_content
    global header_counter
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(header)
    delete_old_marker_content(marker_content)
    marker_content = "<p id='MARKER__CONTENT' style='display:none'>" + str(header_counter) + "</p>"
    header_counter += 1
    message = "\t<div class=\"accordion-header\">\n\t\t<h2 class=\"header-check\">" + header.capitalize() + ' at ' + str(now) + "</h2>\n\t</div>\n\t<div class=\"accordion-content\">\n" + marker_content + "\n\t</div>"
    fin = open("report/report.html", "rt")
    data = fin.read()
    data = data.replace(marker_header, message + "\n" + marker_header)
    fin.close()
    fin = open("report/report.html", "wt")
    fin.write(data)
    fin.close()


def write_success_message(text):
    print(text)
    message = "\t\t<div class=\"success-check\">" + text + "</div>"
    write_string_to_report_file(message)


def write_error_message(text):
    print(text)
    message = "\t\t<div class=\"error-check\">" + text + "</div>"
    write_string_to_report_file(message)


def write_info_message(text):
    print(text)
    message = "\t\t<div class=\"info-message\">" + text + "</div>"
    write_string_to_report_file(message)


def find_element_and_report(driver, parent, selector, type_of_selector, element_name):
    write_info_message('Going to find:"' + element_name + '"')
    try:
        result = get_element_by_selector(parent, selector, type_of_selector)
        write_success_message('Found Element:"' + element_name + '" success!')
        return result
    except NoSuchElementException as ne:
        msg = 'Could not find element:"' + element_name + '" Message:' + ne.msg
        write_error_message(msg)
        return None
    except Exception as e:
        print(e)
        write_error_message(e)
        return None


def click_and_report(driver, element, element_name):
    try:
        write_info_message('Going to click element:"' + element_name + '"')
        ActionChains(driver).move_to_element(element).perform()
        element.click()
        write_success_message('Element:"' + element_name + '" click success!')
        return True
    except Exception as e:
        print(e)
        write_error_message('Error clicking element:"' + element_name + '"')
        write_error_message(e)
        return False


def get_element_by_selector(parent, selector, type_of_selector):
    result = None
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


def find_elements_and_report(driver, parent, selector, type_of_selector, element_name):
    write_info_message('Going to find list of elements:"' + element_name + '"')
    try:
        result = get_elements_by_selector(parent, selector, type_of_selector)
        write_success_message('Found List of Elements:"' + element_name + '" success!')
        return result
    except NoSuchElementException as ne:
        msg = 'Could not find list of elements:"' + element_name + '" Message:' + ne.msg
        write_error_message(msg)
        return None
    except Exception as e:
        print(e)
        write_error_message(e)
        return None


def get_elements_by_selector(parent, selector, type_of_selector):
    result = None
    if type_of_selector == "XPATH":
        result = parent.find_elements(By.XPATH, selector)
    elif type_of_selector == "CLASS_NAME":
        result = parent.find_elements(By.CLASS_NAME, selector)
    elif type_of_selector == "CSS_SELECTOR":
        result = parent.find_elements(By.CSS_SELECTOR, selector)
    elif type_of_selector == "ID":
        result = parent.find_elements(By.ID, selector)
    elif type_of_selector == "NAME":
        result = parent.find_elements(By.NAME, selector)
    elif type_of_selector == "LINK_TEXT":
        result = parent.find_elements(By.LINK_TEXT, selector)
    elif type_of_selector == "PARTIAL_LINK_TEXT":
        result = parent.find_elements(By.PARTIAL_LINK_TEXT, selector)
    elif type_of_selector == "TAG_NAME":
        result = parent.find_elements(By.TAG_NAME, selector)
    return result


def check_current_page(driver, url):
    write_info_message('Going to check if I\'m on url:"' + url + '"')
    if driver.current_url == url:
        write_success_message('I\'m on page:"' + url + '" success')
        return True
    else:
        write_error_message('I\'m not on page:"' + url + '" current url is:"' + driver.current_url)
        return False


def fill_input_and_report(driver, element, text_message, element_name):
    write_info_message('Going to fill element:"' + element_name + '" with text:"' + text_message + '"')
    try:
        ActionChains(driver).move_to_element(element).perform()
        element.click()
        element.send_keys(text_message)
        write_success_message('Data "' + text_message + '" filled successfully!')
        return True
    except Exception as e:
        write_error_message(str(e))
        return False
