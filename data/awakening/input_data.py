import sys
sys.path.append("../../src")

from awakening.repository.AwakeningRepo import *

repo = AwakeningRepo()

file = open("awakening_data.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break

    element = line[:-1].split('\t')

    rotation = 1 if element[0] == "I" else 0
    awakening_name = element[1]
    awakening_aka = "" if element[2] == "0" else element[2]
    description = element[3].replace(":", "\n")
    image = element[4]
    effective_to = "" if element[5] == '0' else " / ".join(element[5:len(element)])

    awakening = repo.get_awakening_by_name(awakening_name)
    if awakening is None:
        repo.add_awakening(rotation, awakening_name, awakening_aka, description, image, effective_to)
    else:
        repo.update_awakening(awakening['id'], rotation, awakening_name, awakening_aka, description, image, effective_to)
