import sys
sys.path.append("../../src")

from ability.repository.CharacterRepository import CharacterRepository

repo = CharacterRepository()

file = open("character_information.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break

    element = line[:-1].split('\t')

    character_name = element[0]
    character = repo.get_character(character_name)
    if character is None:
        character_id = repo.add_character(character_name)
    else:
        character_id = character['id']

    skill_type = element[1]
    skill_name = element[2]
    cooldown = element[3].replace(":", "\n")
    damage = element[4].replace(":", "\n")
    description = element[5]
    image = element[6]
    features = " / ".join(element[7:])

    skill_id = repo.add_skill(skill_name, cooldown, damage, description, features, image)
    repo.link_character_and_skill(character_id, skill_type, skill_id)

