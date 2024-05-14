import os
import sys
print(os.getcwd())
sys.path.append("../../src")

from gear.repository.GearRepo import *

repo = GearRepo()


file = open("gear_data.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break

    element = line[:-1].split('\t')

    name = element[0]
    position = element[1].lower()
    description = element[2].replace(":", "\n")
    image = element[3]

    if position == "forward":
        repo.add_forward_gear(name, image, description)
    else:
        repo.add_goalie_gear(name, image, description)
