from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def wait_until_element_visible(xpath, driver):
    return WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def open_link(link, driver):
    driver = driver.get(link)
    return driver


def click_new_submission_button(driver):
    # click_new_submission_button = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/a",
    # )
    click_new_submission_button = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/a", driver
    )
    click_new_submission_button.click()


def work_with_start_tab(driver):
    # check_box_1 = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[1]/label/input",
    # )
    article = Select(
        driver.find_element(
            By.XPATH,
            value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[1]/div/select",
        )
    )
    # select by visible text
    article.select_by_visible_text("Articles")
    check_box_1 = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[1]/label/input",
        driver,
    )
    check_box_1.click()
    check_box_2 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[2]/label/input",
    )
    check_box_2.click()
    check_box_3 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[3]/label/input",
    )
    check_box_3.click()
    check_box_4 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[4]/label/input",
    )
    check_box_4.click()
    check_box_5 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[2]/ul/li[5]/label/input",
    )
    check_box_5.click()
    check_box_6 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[4]/ul/li[1]/label/input",
    )
    check_box_6.click()
    check_box_7 = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[5]/ul/li/label/input",
    )
    check_box_7.click()
    save_and_continue_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[1]/form/fieldset/div[6]/button",
    )
    save_and_continue_button.click()
    time.sleep(1)


def work_with_upload_submission_tab(driver, file_pdf_name):
    # add_file = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div/div[2]/form/div[2]/div/input",
    # )
    add_file = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div/div[2]/form/div[2]/div/input", driver
    )
    add_file.send_keys(file_pdf_name)
    time.sleep(3)
    article_text = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/ul/li/div/div[2]/span/button[1]",
    )
    article_text.click()
    driver.implicitly_wait(30)
    driver.refresh()
    save_and_continue_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[2]/form/div[3]/button",
    )
    save_and_continue_button.click()


def login_with_username_and_password(username, password, driver):
    driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
    submit_button = driver.find_element(By.CLASS_NAME, "submit")
    submit_button.click()


def fill_the_title(title, driver):
    # fill the title field
    driver.find_element(By.CSS_SELECTOR, '[name="title[en_US]"]').send_keys(title)


def work_with_author(author_and_email, driver):
    original_window = driver.current_window_handle
    click_old_author = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/div[5]/div/table/tbody[1]/tr[1]/td[1]/a",
    )
    click_old_author.click()
    delete_old_author = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/div[5]/div/table/tbody[1]/tr[2]/td/a[2]",
    )
    delete_old_author.click()
    # click ok button to delete author
    driver.implicitly_wait(20)
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # wait to load the window of ojs
    driver.implicitly_wait(50)
    time.sleep(1)
    delete_author_button_accept = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[3]/button[1]",
    )
    delete_author_button_accept.click()
    driver.implicitly_wait(20)
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # wait to load the window of ojs
    driver.implicitly_wait(20)
    # add new correct author
    author = author_and_email[0].split(" ")
    author_name = author[0]
    author_family_name = author[1]
    email = author_and_email[1]
    add_contributor_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/div[5]/div/div[1]/ul/li[2]/a",
    )
    add_contributor_button.click()
    # change driver to new site
    driver.implicitly_wait(20)
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # wait to load the window of ojs
    driver.implicitly_wait(20)
    author_edit_name = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[2]/form/fieldset[1]/div[1]/div[1]/input",
    )
    author_edit_name.send_keys(author_name)
    author_edit_family_name = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[2]/form/fieldset[1]/div[1]/div[2]/input",
    )
    author_edit_family_name.send_keys(author_family_name)
    author_edit_email = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[2]/form/fieldset[1]/div[3]/div/input",
    )
    author_edit_email.send_keys(email)
    author_edit_country = Select(
        driver.find_element(
            By.XPATH,
            value="/html/body/div[5]/div/div[2]/form/fieldset[1]/div[4]/div/select",
        )
    )
    # select by visible text
    author_edit_country.select_by_visible_text("Bulgaria")
    author_combo_box = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[2]/form/fieldset[2]/div[1]/ul/li[1]/label/input",
    )
    author_combo_box.click()
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[2]/form/div[3]/button",
    )
    save_button.click()
    # change driver to new site
    driver.implicitly_wait(20)
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # wait to load the window of ojs
    driver.implicitly_wait(20)
    # ----------------------------#


def fill_the_abstract(abstract, driver):
    # get abstract and fill the abstract field
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, value="iframe"))
    # Insert text via xpath ##
    elem = driver.find_element(By.XPATH, value="/html/body/p")
    elem.send_keys(abstract)
    # Switch back to the "default content" (that is, out of the iframes) ##
    driver.switch_to.default_content()
    # ----------------------------#


def fill_the_keywords(keywords, driver):
    # fill the keywords field
    keywords_edit = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/fieldset/div[1]/ul/li/input",
    )
    # keywords_edit = driver.find_element(By.CLASS_NAME, value="ui-widget-content")
    # elem1 = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    keywords_edit.click()
    keywords_edit.send_keys(keywords[0])
    keywords_edit.send_keys(Keys.ENTER)
    for i in range(1, len(keywords)):
        xpath = (
            "/html/body/div[1]/div[1]/main/div/div/div[3]/form/fieldset/div/ul/li["
            + str(i + 1)
            + "]/input"
        )
        keywords_edit = driver.find_element(
            By.XPATH,
            value=xpath,
        )
        keywords_edit.send_keys(keywords[i])
        keywords_edit.send_keys(Keys.ENTER)
    # ----------------------------#


# language: Bulgarian
def fill_the_language(language, driver):
    language_edit = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/fieldset[2]/div[1]/ul/li/input",
    )
    language_edit.send_keys(language)
    # language_edit.send_keys("English")
    language_edit.send_keys(Keys.ENTER)


# type: text
def fill_the_type_and_right(link_for_publication_metadata, type, right, driver):
    # fill the type field with text
    driver.get(link_for_publication_metadata)
    language_edit = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[4]/form/div/div/fieldset/div/div[2]/div/div/div[2]/div[2]/div[1]/input",
        driver,
    )
    language_edit.send_keys("English")
    language_edit.send_keys(Keys.ENTER)
    type_edit = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[4]/form/div/div/fieldset/div/div[4]/div/div/div[2]/div/input",
        driver,
    )
    type_edit.clear()
    type_edit.send_keys(type)
    rights_edit = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[4]/form/div/div/fieldset/div/div[3]/div/div/div[2]/div/input",
    )
    rights_edit.clear()
    rights_edit.send_keys(right)
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[4]/form/div/div/div/div/button",
    )
    save_button.click()
    time.sleep(1)


# right: open
def fill_the_right(right, driver):
    # fill the right field with open
    # driver.get(link_for_publication_metadata)
    rights_edit = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/fieldset[1]/div[3]/div/input",
    )
    rights_edit.clear()
    rights_edit.send_keys(right)


def fill_the_type(type, driver):
    # fill the right field with open
    # driver.get(link_for_publication_metadata)
    type_edit = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/fieldset[1]/div[2]/div/input",
    )
    type_edit.clear()
    type_edit.send_keys(type)


def fill_the_reference(link_for_publication_references, references, driver):
    # references = references.replace(".\n", "$$")
    # references = references.replace("\n", "")
    # references = references.replace("$$", ".\n")
    driver.get(link_for_publication_references)
    time.sleep(1)
    reference_edit = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/form/div/div/fieldset/div/div/div[3]/textarea",
        driver,
    )
    reference_edit.clear()
    reference_edit.send_keys(references)
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/form/div/div/div/div/button",
    )
    save_button.click()
    time.sleep(1)


def click_save_and_continue_button(driver):
    save_and_continue_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[3]/form/div[6]/button",
    )
    save_and_continue_button.click()
    time.sleep(1)


def wait(driver):
    original_window = driver.current_window_handle
    driver.implicitly_wait(20)
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # wait to load the window of ojs
    driver.implicitly_wait(20)
    return driver


def click_finish_submission_button(driver):
    finish_submission_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div/div[4]/form/div[2]/button",
    )
    finish_submission_button.click()
    time.sleep(1)


def click_confirm_finish_submission(driver):
    confirm_finish_submission = driver.find_element(
        By.XPATH,
        value="/html/body/div[5]/div/div[3]/button[1]",
    )
    confirm_finish_submission.click()


def work_with_license_tab(
    link_for_publication_license, name_of_the_book, copyright_year_value, driver
):
    driver.get(link_for_publication_license)
    # enter copyright holder
    # copyright_holder_override_button = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div[1]/div/div/div[3]/div/button",
    # )
    copyright_holder_override_button = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[8]/form/div/div/fieldset/div/div[1]/div/div/div[3]/div/button",
        driver,
    )
    copyright_holder_override_button.click()
    time.sleep(1)
    copyright_holder = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[8]/form/div/div/fieldset/div/div[1]/div/div/div[3]/div/input",
    )
    copyright_holder.send_keys(name_of_the_book)
    # enter copyright year
    copyright_year_override_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[8]/form/div/div/fieldset/div/div[2]/div[3]/div/button",
    )
    copyright_year_override_button.click()
    time.sleep(1)
    copyright_year = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[8]/form/div/div/fieldset/div/div[2]/div[3]/div/input",
    )
    copyright_year.send_keys(copyright_year_value)
    # click button save
    save_of_license_tab_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[8]/form/div/div/div/div/button",
    )
    save_of_license_tab_button.click()
    time.sleep(1)


def work_with_issue_tab(
    link_for_publication_issue, pages, date_published_value, driver
):
    driver.get(link_for_publication_issue)
    # enter pages
    # pages_textfield = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/form/div/div/fieldset/div/div[4]/div[2]/div/input",
    # )
    pages_textfield = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[9]/form/div/div/fieldset/div/div[4]/div[2]/div/input",
        driver,
    )
    pages_textfield.send_keys(pages)
    # enter date published
    date_published_textfield = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[9]/form/div/div/fieldset/div/div[6]/div[3]/div/input",
    )
    date_published_textfield.send_keys(date_published_value)
    # click save
    save_of_issue_tab_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[9]/form/div/div/div/div/button",
    )
    save_of_issue_tab_button.click()
    time.sleep(1)


def work_with_galleys_tab(link_for_publication_galleys, file_pdf_name, driver):
    driver.get(link_for_publication_galleys)
    # driver = wait(driver)
    # driver.implicitly_wait(30)

    # add_galley_button = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/div/div/div[1]/ul/li[2]/a",
    # )
    # wait_until_element_visible("/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/div/div",driver)
    # driver = wait(driver)
    # ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
    # add_galley_button = wait_until_element_visible("/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/div/div/div[1]/ul/li[2]/a",driver)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (
                By.XPATH,
                "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/div/div/div[1]/h4",
            ),
            "Galleys",
        )
    )
    # add_galley_button = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions)\
    #                     .until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[5]/div/div/div[1]/ul/li[2]/a")))
    add_galley_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/div/div/div[1]/ul/li[2]/a",
    )
    driver.implicitly_wait(20)
    add_galley_button.click()
    driver = wait(driver)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (
                By.XPATH,
                "/html/body/div[3]/div/div[2]/form/fieldset/div[1]/label/text()",
            ),
            "Galley Label",
        )
    )
    galleys_label_textfield = driver.find_element(
        By.XPATH,
        value="/html/body/div[4]/div/div[2]/form/fieldset/div[1]/div/input",
    )
    galleys_label_textfield.send_keys("PDF")
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/form/div/button",
    )
    save_button.click()
    driver = wait(driver)
    select_article = Select(
        driver.find_element(
            By.XPATH,
            value="/html/body/div[3]/div/div[2]/div[1]/div[1]/form/fieldset/div[1]/div/select",
        )
    )
    select_article.select_by_visible_text("Article Text")
    driver = wait(driver)
    upload_file = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/div[1]/div[1]/form/fieldset/div[2]/div/div[2]/div[4]/input",
    )
    upload_file.send_keys(file_pdf_name)
    driver = wait(driver)
    continue_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/div[2]/button",
    )
    continue_button.click()
    driver = wait(driver)
    continue_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/div[2]/button",
    )
    continue_button.click()
    driver = wait(driver)
    complete_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/div[2]/button",
    )
    complete_button.click()
    time.sleep(1)


def work_with_publication(link_for_publication_license, issue_value, driver):
    driver.get(link_for_publication_license)
    # driver = wait(driver)
    # driver.implicitly_wait(30)
    # schedule_for_publication_button = driver.find_element(
    #     By.XPATH,
    #     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[1]/div/button",
    # )
    schedule_for_publication_button = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[1]/div/button", driver
    )
    driver.execute_script("arguments[0].click();", schedule_for_publication_button)
    # schedule_for_publication_button.click()
    driver = wait(driver)
    select_issue = wait_until_element_visible(
        "/html/body/div[4]/div/div[2]/div/form/div/div/fieldset/div/div/div[2]/select",
        driver,
    )
    select_issue = Select(select_issue)
    select_issue.select_by_value(issue_value)
    driver.refresh()
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[3]/div/div[2]/div/form/div/div/div/div/button",
    )
    save_button.click()
    time.sleep(1)


def work_with_doi(link_for_publication_doi, doi_data, driver):
    driver.get(link_for_publication_doi)
    substring = ""
    if "https://doi.org/" in doi_data:
        # print(page.get_text())
        split_text = doi_data.split("https://doi.org/", 1)
        substring = split_text[1]
    doi_text_field = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div/div[3]/div/input",
        driver,
    )
    doi_text_field.clear()
    doi_text_field.send_keys(substring)
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/div/div/button",
    )
    save_button.click()
    time.sleep(1)


def clear_doi(link_for_publication_doi, driver):
    driver.get(link_for_publication_doi)
    doi_text_field = wait_until_element_visible(
        "/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div/div[3]/div/input",
        driver,
    )
    doi_text_field.clear()
    save_button = driver.find_element(
        By.XPATH,
        value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/div/div/button",
    )
    save_button.click()
    time.sleep(2)
