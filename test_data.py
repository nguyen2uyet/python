with open("data.txt", "r", encoding="utf-8") as file_3:
    data = file_3.read()

list_of_data = data.split("\n$$\n")

for list_of_description in list_of_data:
    list_of_description = list_of_description.splitlines()
    print(list_of_description[0])
    print(list_of_description[1])
    print(list_of_description[2])
    print(list_of_description[3])
    print(list_of_description[4])
    print(list_of_description[5])
    print(list_of_description[6])
