# __missing__ gdy nie znajdzie klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "Default"


d_python = {}
print(type(d_python))  # <class 'dict'>
# print(d_python['name'])  # KeyError: 'name'

d1 = DefaultDict()
print(d1)  # {}
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1['name'])  # Default


# słownik e którym gdy jak nie ma klucza, tworzy taki klucz z wartością domyslną np.: 0
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


a1 = AutoKeyDict()
print(a1)  # {}
print(a1['name'])  # name
print(a1)  # {'name': 0}


# zamienia klucze na małe litery
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self.get(key.lower())
        if isinstance(key, str):
            return self[key.lower()]
        return key


c1 = CaseInsensitiveDict()
c1['name'] = "Radek"
print(c1['Name'])  # Radek
c1[1] = "tekst"
print(c1)  # {'name': 'Radek', 1: 'tekst'}
print(c1[1])  # tekst
