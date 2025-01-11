class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year

    def get_info(self):
        return "Название книги: " + self.title + ", Автор: " + self.author + ", Год издания: " + str(self.year)

mybook = Book("Преступление и Наказание", "Фёдор Достоевский", 1866)
print(mybook.get_info())


class Circle:
    def __init__(self, radius):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def set_radius(self, r):
        self.radius=r

cake = Circle(12)
print("У тортика радиус", cake.get_radius(), "сантиметров!")
cake.set_radius(0)
print("Теперь радиус тортика " + str(cake.get_radius()) + "... мне ничего не оставили :(")
