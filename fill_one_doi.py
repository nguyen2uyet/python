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
sub_name_of_the_digital_book = "DASC"
name_of_the_book = "Digital Age in Semiotics & Communication"
copyright_year_value = "2022"
issue_value = "60"
split_symbol_of_keywords = ";"
date_published_value = "2022-12-30"
root = r"C:\Users\nguye\Desktop\13_Yearbook of department Administration and management_vol 5_2020_za PORTAL"


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


# list_of_description = list_of_description.splitlines()
# INIT DATA
# ---------------------------------------------
# get title
# title = list_of_description[0]
# # get author and email
# author_and_email = list_of_description[1].split(",")
# # get the keywords
# keywords = list_of_description[2].split(split_symbol_of_keywords)
# # get abstract
# abstract = list_of_description[3]
# # get number of submission
# number_of_submission = list_of_description[4]
# # get page
# pages = list_of_description[5]
# # get file name
# file_name = list_of_description[6]
# # name of file pdf
# file_pdf_name = root + "\\" + file_name
# get doi
number_of_submission = 750
# list_of_description = list_of_description.split("\n")
doi = list_of_description[0]
references = list_of_description[1:]
print("\n".join(references))
link_for_publication = (
    "https://ojs.nbu.bg/index.php/"
    + sub_name_of_the_digital_book
    + "/workflow/index/"
    + str(number_of_submission)
    + "/4#publication"
)
link_for_publication_license = link_for_publication + "/license"
link_for_publication_issue = link_for_publication + "/issue"
link_for_publication_galleys = link_for_publication + "/galleys"
link_for_publication_doi = link_for_publication + "/identifiers"
link_for_publication_references = link_for_publication + "/citations"
link_for_publication_metadata = link_for_publication + "/metadata"
# ---------------------------------------------
# fill doi field
work_with_doi(link_for_publication_doi, doi, driver)
# fill text
fill_the_type_and_right(link_for_publication_metadata, "text", "open", driver)
# fill right
# fill_the_right(link_for_publication_metadata, "open", driver)
# fill references
fill_the_reference(link_for_publication_references, references, driver)
number_of_submission = number_of_submission + 1
# time.sleep(2000)
