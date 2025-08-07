# stworzyc system zarządzania biblioteką
# Book
# dodanie ksiązek, wypożyczenie ksiazek, zwrrot ksiązki
# obsłużyc błedy
# dodać kalsę Library
# title, author, isbn
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"


book = Book('Pan Tadeusz', "Adam Mickiewicz", "1234567890")
print(book)  # Author: 'Adam Mickiewicz', Tytuł: 'Pan Tadeusz', ISBN: '1234567890'


class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.append(book)
                self.dostepne_ksiazki.remove(book)
                return book
        raise Exception("Nie ma takiej ksiązki")

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return book
        raise Exception("Ksiązka  nie z naszej biblioteki")
