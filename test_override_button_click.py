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
import time

# open and get data from txt files
with open("description.txt", "r", encoding="utf-8") as file_1:
    list_of_description = file_1.read().splitlines()

with open("references.txt", "r", encoding="utf-8") as file_2:
    references = file_2.read()


number_of_submission = list_of_description[4]
pages = list_of_description[5]

# ------------------
# need to change with new book
sub_name_of_the_digital_book = "EcoBY"
name_of_the_book = "Еconomy and Business Yearbook"
copyright_year_value = "2020"
split_symbol_of_keywords = ","
date_published_value = "2020-12-30"

link = (
    "https://ojs.nbu.bg/index.php/"
    + sub_name_of_the_digital_book
    + "/submission/wizard/3?submissionId="
    + number_of_submission
)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(link)

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

# username = "student"
username = "dmladenova"
driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)

# password = "Student@01"
password = "#EI1316"
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)


submit_button = driver.find_element(By.CLASS_NAME, "submit")
submit_button.click()

# wait to load the window of ojs
driver.implicitly_wait(20)

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# wait to load the window of ojs
driver.implicitly_wait(50)


# ----------------------------#

link_for_publication = (
    "https://ojs.nbu.bg/index.php/"
    + sub_name_of_the_digital_book
    + "/workflow/index/"
    + number_of_submission
    + "/1#publication"
)

link_for_publication_license = link_for_publication + "/license"

link_for_publication_issue = link_for_publication + "/issue"

link_for_publication_galleys = link_for_publication + "/galleys"

# enter copyright holder and copyright year in license tab
# open license tab
# driver.get(link_for_publication_license)

# wait = WebDriverWait(driver, 10)

# original_window = driver.current_window_handle

# # enter copyright holder
# copyright_holder_override_button = driver.find_element(
#     By.XPATH,
#     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div[1]/div/div/div[3]/div/button",
# )

# copyright_holder_override_button.click()


# copyright_holder = driver.find_element(
#     By.XPATH,
#     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div[1]/div/div/div[3]/div/input",
# )

# copyright_holder.send_keys(name_of_the_book)

# # enter copyright year

# copyright_year_override_button = driver.find_element(
#     By.XPATH,
#     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div[2]/div[3]/div/button",
# )

# copyright_year_override_button.click()

# copyright_year = driver.find_element(
#     By.XPATH,
#     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/fieldset/div/div[2]/div[3]/div/input",
# )

# copyright_year.send_keys(copyright_year_value)

# # click button save

# save_of_license_tab_button = driver.find_element(
#     By.XPATH,
#     value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[6]/form/div/div/div/div/button",
# )

# save_of_license_tab_button.click()

# enter pages and date published in issue tab
# open issue tab
driver.get(link_for_publication_issue)

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

# enter pages

pages_textfield = driver.find_element(
    By.XPATH,
    value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/form/div/div/fieldset/div/div[4]/div[2]/div/input",
)

pages_textfield.send_keys(pages)

# enter date published

date_published_textfield = driver.find_element(
    By.XPATH,
    value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/form/div/div/fieldset/div/div[6]/div[3]/div/input",
)

date_published_textfield.send_keys(date_published_value)

# click save

save_of_issue_tab_button = driver.find_element(
    By.XPATH,
    value="/html/body/div[1]/div[1]/main/div/div[2]/div[3]/div/div[2]/div[7]/form/div/div/div/div/button",
)

save_of_issue_tab_button.click()

# open galleys
