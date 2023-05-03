import re

list_of_data = []
with open("file.txt", "r", encoding="utf-8") as file:
    list_of_data = file.read().splitlines()

list_of_data_1 = re.sub("\s+", " ", list_of_data[1]).lstrip().split(" ")
list_of_data_last = (
    re.sub("\s+", " ", list_of_data[len(list_of_data) - 1]).lstrip().split(" ")
)

print(list_of_data_last)

credit = list_of_data_1[7]
year = list_of_data_1[8]
subject = list_of_data[0]
protocol = list_of_data_last[1]
score = list_of_data_last[3]


final_data = subject + "\t" + credit + "\t" + year + "\t" + protocol + "\t" + score


with open("file.txt", "w", encoding="utf-8") as file:
    file.write(final_data)
