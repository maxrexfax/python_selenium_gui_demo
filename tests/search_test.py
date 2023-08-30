import time
import functions.reportHelper as rp


def search_test(driver, url, text_to_search):
    rp.write_header("Search test starts")
    rp.write_info_message("Testing of duckduckgo search starts")
    driver.get(url)
    time.sleep(3)
    is_on_page = rp.check_current_page(driver, url)
    if not is_on_page:
        rp.write_error_message('Not on target url, cannot perform further test, stop test!')
        return

    input_for_search = rp.find_element_and_report(driver, driver,
                                                      'searchbox_input',
                                                      'ID',
                                                      'Search input')
    if input_for_search is not None:
        fill_result = rp.fill_input_and_report(driver, input_for_search, text_to_search, 'Input for search')
    else:
        rp.write_error_message(
            'Cannot continue step get "Fill Search input" - element not found - stop test')
        return

    if fill_result is True:
        form = rp.find_element_and_report(driver, driver,
                                                      'searchbox_homepage',
                                                      'ID',
                                                      'Search form')
    else:
        rp.write_error_message('Cannot continue step "Find search FORM" - Filling input failed - stop test')
        return

    if form is not None:
        button_search = rp.find_element_and_report(driver, form,
                                                      '//button[@type="submit"]',
                                                      'XPATH',
                                                      'Search button')
    else:
        rp.write_error_message('Cannot continue step "Find search button" - FORM NOT FOUND - stop test')
        return
    if button_search is not None:
        rp.click_and_report(driver, button_search, 'Search button')
    else:
        rp.write_error_message('Cannot continue step "Click search button" - BUTTON NOT FOUND - stop test')
        return

