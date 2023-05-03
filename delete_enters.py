with open("file_1.txt", "r", encoding="utf-8") as file:
    text = file.read()


text = text.replace("\n", " ")


with open("file_1.txt", "w", encoding="utf-8") as file:
    file.write(text)
    file.write("\n")
