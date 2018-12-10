def get_name_score(name):

    character_offset = 64
    name_score = 0

    for character in name:
        name_score += ord(character) - character_offset

    return name_score


file = open("names.txt", "r")

names = file.readline().replace('"', '').split(',')

names.sort()

for_offset = 1
summarized_names_score = 0

for index in range(0, names.__len__()):
    summarized_names_score += get_name_score(names[index] * (index + for_offset))

print(summarized_names_score)
