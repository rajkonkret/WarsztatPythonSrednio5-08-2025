from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


class Contact:
    all_contacts = ContactList()  # lista wspólna dla wszystkich obiektów klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__
    def __repr__(self):  # repr nadpisuje str, gdy str nie jest zdefiniowany
        return f"{self.name} {self.email}"
        # return f"{self.name, self.email}" to by była krotka


class Suplier(Contact):
    """"
    Klasa dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


# klasa Friend, dziedziczy po Suplier
# __repr__

class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() - musimy wywołąc obowiązkowo kontruktor klasy wyższej
        self.phone = phone

    def __repr__(self):  # repr nadpisuje str, gdy str nie jest zdefiniowany
        # !r - teksty w cudzysłowach
        return f"{self.name!r} {self.email!r}, +48{self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)
# AttributeError: 'list' object has no attribute 'search'
# po zdefiniowaniu listy ContactList
print(c3.all_contacts.search("Radek"))  # [Radek radek@wp.pl]

f1 = Friend("Kasia", "kasia@onet.pl")
f2 = Friend("Kamil", "kamil@onet.pl")
print(f1, f2)
# Kasia kasia@onet.pl Kamil kamil@onet.pl

print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Kasia kasia@onet.pl, Kamil kamil@onet.pl]
print(Contact.all_contacts.search("Kasia"))  # [Kasia kasia@onet.pl]
# [Kasia kasia@onet.pl, +48000000000]
f3 = Friend("Aneta", "aneta@wp.pl", "654678098")
print(f3)  # Aneta aneta@wp.pl, +48654678098
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Kasia kasia@onet.pl, +48000000000, Kamil kamil@onet.pl, +48000000000, Aneta aneta@wp.pl, +48654678098]

pprint(Contact.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Kasia kasia@onet.pl, +48000000000,
#  Kamil kamil@onet.pl, +48000000000,
#  Aneta aneta@wp.pl, +48654678098]

# kolejnośc rozwiazywania nazw metod dla obiektu
pprint(Friend.__mro__)
# (<class '__main__.Friend'>,
#  <class '__main__.Suplier'>,
#  <class '__main__.Contact'>,
#  <class 'object'>)
