class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
GuysCar = Car("Mitzubishi", "lancer", "2007", "grey")
# print(GuysCar.brand, GuysCar.model, GuysCar.year, GuysCar.color)

class Book:
    def __init__(self, title, author, pages, genre):
       self.title = title
       self.author = author
       self.pages = pages
       self.genre = genre
HarryPotter = Book("HarryPotter", "J-K_Rolling", "200", "fiction")
# print(HarryPotter.title, HarryPotter.author)

