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
    if input_for_search is None:
        rp.write_error_message(
            'Stop test on step "Find Search input" - element not found')
        return
    fill_result = rp.fill_input_and_report(driver, input_for_search, text_to_search, 'Input for search')

    if fill_result is False:
        rp.write_error_message('Stop test on step "Fill search FORM"')
        return

    form = rp.find_element_and_report(driver, driver,
                                                  'searchbox_homepage',
                                                  'ID',
                                                  'Search form')
    if form is None:
        rp.write_error_message('Stop test on step "Find form" - element not found')
        return

    button_search = rp.find_element_and_report(driver, form,
                                               '//button[@type="submit"]',
                                               'XPATH',
                                               'Search button')

    if button_search is None:
        rp.write_error_message('Stop test on step "Find search button" - element not found')
        return

    click_result = rp.click_and_report(driver, button_search, 'Search button')

    if click_result is False:
        rp.write_error_message('Stop test on step "Click search button"')
        return
