import os
print(os.getcwd())

file = open("character_data.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break

    element = line[:-1].split('\t')

    if element[0] == "젠타로":
        print("oops")

    print(element)
