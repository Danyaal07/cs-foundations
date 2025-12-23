people = {
    "Danyaal" : 18,
    "Duaa" : 17, 
    "Imaad" : 16
    }

def insert(people, key, value):
    if key not in people:
        people[key] = value
    else:
        print("Value already exists")

def update(people, key, value):
    if key in people:
        people[key] = value
    else:
        print("Value does not exist. Can't update.")

def delete(people, key):
    if key in people:
        del people[key]
    else:
        print("Value not found")

def display(people):
    for name, age in people.items():
        print(f"{name} is {age} years old")

insert(people, "Danyaal", 10)
insert(people, "Bob", 20)
update(people, "Imaad", 17)
delete(people, "Duaa")
display(people)