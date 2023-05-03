from docx import Document
import mammoth

# importing re module
import re

file_name = r"C:\Users\nguye\Desktop\Thi Lai\Autumn\CSCB732 Софтуерен инженеринг\Tema10-ДОКУМЕНТИРАНЕ НА СОФТУЕРА.docx"
# document = Document(file_name)

# custom_styles = "b => i"

with open(file_name, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    text = result.value
    with open("output.txt", "w", encoding="utf-8") as html_file:
        html_file.write(text)

res_1 = ""
res_2 = ""

with open("output.txt", "r", encoding="utf-8") as html_file:
    # initializing string
    test_str = html_file.read()

    # printing original string
    # print("The original string is : " + str(test_str))

    # initializing tag
    tag_1 = "strong"
    tag_2 = "li"

    # regex to extract required strings
    reg_str_1 = "<" + tag_1 + ">(.*?)</" + tag_1 + ">"
    reg_str_2 = "<" + tag_2 + ">(.*?)</" + tag_2 + ">"
    res_1 = re.findall(reg_str_1, test_str)
    res_2 = re.findall(reg_str_2, test_str)

    # printing result
    # print("The Strings extracted : " + str(res))

with open("output.txt", "w", encoding="utf-8") as html_file:
    for s in res_1:
        html_file.write(s)
        html_file.write("\n")
    # for s in res_2:
    #     html_file.write(s)
    #     html_file.write("\n")
