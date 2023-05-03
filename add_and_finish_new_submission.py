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
from fill_form_submission import *
import time

# open and get data from txt files
# with open("description.txt", "r", encoding="utf-8") as file_1:
#     list_of_description = file_1.read().splitlines()

# with open("references.txt", "r", encoding="utf-8") as file_2:
#     references = file_2.read()

with open("data.txt", "r", encoding="utf-8") as file_3:
    data = file_3.read()

list_of_data = data.split("\n$$\n")

# ------------------
# need to change with new book
sub_name_of_the_digital_book = "ANSD"
name_of_the_book = "Annual of Natural Sciences Department"
copyright_year_value = "2022"
issue_value = "61"
split_symbol_of_keywords = ","
date_published_value = "2022-12-30"
root = r"C:\Users\nguye\Desktop\20_Godishnik_Prirodni_nauki_2022_Vol_7\New folder"


# access the link and login to ojs.nbu.bg with username and password

# link = (
#     "https://ojs.nbu.bg/index.php/"
#     + sub_name_of_the_digital_book
#     + "/submission/wizard/3?submissionId="
#     + number_of_submission
# )
link_for_new_submission = (
    "https://ojs.nbu.bg/index.php/"
    + sub_name_of_the_digital_book
    + "/submissions#myQueue"
)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(link_for_new_submission)


# username = "student"
username = "dmladenova"

# password = "Student@01"
password = "#EI1316"


# Step 1: Login with username and password
login_with_username_and_password(username, password, driver)
# Wait for new window
driver = wait(driver)

# get number of submission
frist_number_of_submission = 863


for list_of_description in list_of_data:
    list_of_description = list_of_description.splitlines()
    # INIT DATA
    # ---------------------------------------------
    # get title
    title = list_of_description[0]
    # get author and email
    author_and_email = list_of_description[1].split(",")
    # get page
    pages = list_of_description[2]
    # get the doi
    doi_data = list_of_description[3]
    # get abstract
    abstract = list_of_description[4]
    # get the keywords
    keywords = list_of_description[5].split(split_symbol_of_keywords)

    # get file name
    file_name = list_of_description[6]
    # get references
    references = list_of_description[7:]

    # ---------------------------------------------
    # Create new submission
    # name of file pdf
    file_pdf_name = root + "\\" + file_name
    link_for_publication = (
        "https://ojs.nbu.bg/index.php/"
        + sub_name_of_the_digital_book
        + "/workflow/index/"
        + str(frist_number_of_submission)
        + "/4#publication"
    )
    link_for_publication_license = link_for_publication + "/license"
    link_for_publication_doi = link_for_publication + "/identifiers"
    link_for_publication_issue = link_for_publication + "/issue"
    link_for_publication_galleys = link_for_publication + "/galleys"
    link_for_publication_metadata = link_for_publication + "/metadata"
    link_for_publication_references = link_for_publication + "/citations"
    link_for_enter_metadata = (
        "https://ojs.nbu.bg/index.php/ANSD/submission/wizard/3?submissionId="
        + str(frist_number_of_submission)
    )
    driver.get(link_for_enter_metadata)
    # click_new_submission_button(driver)
    # # Wait for new window
    # driver = wait(driver)
    # # Work with tab start
    # work_with_start_tab(driver)
    # # Wait for new window
    # driver = wait(driver)
    # # Work with tab upload submission
    # work_with_upload_submission_tab(driver, file_pdf_name)
    # # Step 2: Get title and fill the title field

    fill_the_title(title, driver)
    # Step 3: Work with author
    work_with_author(author_and_email, driver)
    # Step 4: Fill the abstract
    fill_the_abstract(abstract, driver)
    # Step 5: Fill the keywords
    fill_the_keywords(keywords, driver)
    # Step 5.5: Fill the right
    fill_the_right("open", driver)
    # Step 5.6: Fill the type
    fill_the_type("text", driver)
    # Step 6: Fill the save and continue button
    click_save_and_continue_button(driver)
    # # Step 7: Change to new driver
    driver = wait(driver)
    # # Step 8: Click finish submission
    click_finish_submission_button(driver)
    # Step 9: Change to new driver
    driver = wait(driver)
    time.sleep(1)
    # Step 10: Click confirm finish submisson button
    # click_confirm_finish_submission(driver)
    # Step 11: Work with license tab
    work_with_license_tab(
        link_for_publication_license, name_of_the_book, copyright_year_value, driver
    )
    # Step 4: Fill the references
    fill_the_reference(link_for_publication_references, references, driver)
    # Step 11.1: Work with doi
    work_with_doi(link_for_publication_doi, doi_data, driver)
    # Step 11.1: Work with right
    # fill_the_type_and_right(link_for_publication_metadata, "text", "open", driver)
    # Step 12: Work with issue tab
    work_with_issue_tab(link_for_publication_issue, pages, date_published_value, driver)
    # Step 13: Work with galleys tab
    work_with_galleys_tab(link_for_publication_galleys, file_pdf_name, driver)
    # Wait for new window
    # driver = wait(driver)
    # Step 14: Work with publication
    work_with_publication(link_for_publication_galleys, issue_value, driver)
    frist_number_of_submission = frist_number_of_submission + 1

time.sleep(2000)
