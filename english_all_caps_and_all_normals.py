with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.replace(".\n", "$$")
text = text.replace("\n", "")
text = text.replace("$$", ".\n")

text1 = text.lower()

with open("file.txt", "w", encoding="utf-8") as file:
    file.write(text)
    file.write("\n")
    file.write(text1)
    file.write("\n")
