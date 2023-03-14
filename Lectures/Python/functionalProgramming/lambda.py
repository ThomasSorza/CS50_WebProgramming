people = [
    {"name": "harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#lambda is a function
people.sort(key=lambda person: person["name"])

print(people)