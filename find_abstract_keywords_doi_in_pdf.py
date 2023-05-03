import sys
import fitz
import re
import os
import datetime


def delete_enters(text):
    text = text.replace(".\n", "$$")
    text = text.replace("\n", "")
    text = text.replace("$$", ".\n")
    return text


folder_path = r"C:\Users\nguye\Desktop\11_Ikonomika-i-biznes-2020_za PORTAL\New folder"
all_text = ""
files = os.listdir(folder_path)
files = [
    (filename, os.path.getctime(os.path.join(folder_path, filename)))
    for filename in files
    if os.path.isfile(os.path.join(folder_path, filename))
]
files.sort(key=lambda x: x[1])

for file in files:
    # print(file[0])
    for fname in file[0].split("\n"):
        file_path = os.path.join(folder_path, fname)
        if os.path.isfile(file_path):
            doc = fitz.open(file_path)
            # get doi
            page_1 = doc[0]
            page_2 = doc[1]
            wlist = page_1.get_text() + page_2.get_text()
            doi_text = ""
            pattern = re.compile(r"doi.org")
            for line in wlist.split("\n"):
                if pattern.search(line):
                    doi_text = line
                    break
            all_text = all_text + doi_text
            references = "\n\n"
            for page in doc:
                if "Литература" in page.get_text():
                    # print(page.get_text())
                    split_text = page.get_text().split("Литература", 1)
                    substring = split_text[1]
                    pattern = re.compile(r"^[^0-9]")
                    references = delete_enters(substring)
                    # for line in substring.split("\n"):
                    #     if pattern.search(line):
                    #         # print(line)
                    #         references = references.replace("\n" + line, line)
                    #         # print(line)
                    break
            all_text = all_text + references + "$$\n"

with open("file.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

# root = r"C:\Users\nguye\Desktop\13_Yearbook of department Administration and management_vol 5_2020_za PORTAL\godishnik-departament-administratsia-i-upravlenie-2020-"
# fname_pages = "9-22"
# fname = root + fname_pages + ".pdf"

# with open("file.txt", "r", encoding="utf-8") as file:
#     text = file.read()


# page_1 = doc[0]
# page_2 = doc[1]

# wlist = page_1.get_text() + page_2.get_text()
# print(wlist)


# abstract_text = ""
# keyword_text = ""
# doi_text = ""
# pages_text = ""
# all_caps_cyrillic_text = ""
# all_caps_english_text = ""
# references = ""

# get all caps words in cyrillic

# all_caps_cyrillic = re.search(r"^[А-ЯЁ\s\.\-]+\n", wlist, re.MULTILINE)

# if all_caps_cyrillic:
#     all_caps_cyrillic_text = delete_enters(all_caps_cyrillic.group())

# # get all caps words in english

# all_caps_english = re.search(r"^[A-Z\.\-\s]+\n", wlist, re.MULTILINE)

# if all_caps_english:
#     all_caps_english_text = delete_enters(all_caps_english.group())

# # get abstract
# abstract = re.search(r"Abstract:(.*?)Keywords:", wlist, re.DOTALL)

# if abstract:
#     abstract_text = delete_enters(abstract.group(1).strip())

# # get keywords
# keyword = re.search(r"Keywords:(.*?)doi", wlist, re.DOTALL)

# if keyword:
#     keyword_text = delete_enters(keyword.group(1).strip())

# # get doi
# doi = re.search(r"^doi.*", wlist, re.MULTILINE)
# if doi:
#     doi_text = doi.group()

# # get pages
# end_page = re.search(r"\d+(?=\.\w+)", fname)
# if end_page:
#     end_page_number = int(end_page.group())
#     length = len(doc)
#     pages_text = str(end_page_number - length) + "-" + str(end_page_number - 1)

# get references


# with open("file.txt", "w", encoding="utf-8") as file:
#     file.write(all_caps_cyrillic_text)
#     file.write("\n")
#     file.write(all_caps_english_text)
#     file.write("\n")
#     file.write(all_caps_english_text.lower())
#     file.write("\n")
#     file.write(abstract_text)
#     file.write("\n")
#     file.write(keyword_text)
#     file.write("\n")
#     file.write(doi_text)
#     file.write("\n")
#     file.write(pages_text)
