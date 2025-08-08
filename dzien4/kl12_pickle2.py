import pickle
from kl11_dataclass import Person

with open('dane.pckl', "rb") as file:
    p = pickle.load(file)

print("----------")
print(p)
# [Person(first_name='Jan', last_name='Kowalski', id=1),
# Person(first_name='Maciej', last_name='Arbuz', id=2)]

for person in p:
    person.greets()
# my name is: Jan
# my name is: Maciej
