file = open("/data/character_information.txt", "r")

while True:
    line = file.readline()
    if not line:
        break

    element = line[:-1].split('\t')

    print(element)
