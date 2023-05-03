with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

# replace enter with comma
text = text.replace("\n", ",")

with open("file.txt", "w", encoding="utf-8") as file:
    file.write(text)
    file.write("\n")
