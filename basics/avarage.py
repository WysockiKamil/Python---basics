people = [
    {"name": "Anna", "age": 25},
    {"name": "Kamil", "age": 31},
    {"name": "Zosia", "age": 19}
]

# 1) wypisz osoby pełnoletnie
for person in people:
    if person["age"] >= 18:
        print(f"{person['name']} jest pełnoletni(a)")

# 2) oblicz średni wiek
sorted_people = sorted(people, key=lambda x: x["age"])
print("Posortowane osoby według wieku:")
for sorted_person in sorted_people:
   print(f"{sorted_person['name']} - {sorted_person['age']} lat")        

#3) oblicz średni wiek
total_age = sum(person["age"] for person in people)
average_age = total_age / len(people)
print(f"Średni wiek osób to: {average_age:.2f} lat")

# 4) wypisz osoby w wieku poniżej średniej
for person in people:
    if person["age"] < average_age:
        print(f"{person['name']} jest poniżej średniej wieku ({average_age:.2f} lat)")

# 5) wypisz osoby w wieku powyżej średniej
for person in people:
    if person["age"] > average_age:
        print(f"{person['name']} jest powyżej średniej wieku ({average_age:.2f} lat)")