import pickle

# 1. Создание базового класса Animal

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def eat(self):
        print(f"{self.name} ест.")

# 2. Создание подклассов Bird, Mammal, и Reptile

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def __str__(self):
        return f"Птица: {super().__str__()}, размах крыльев: {self.wingspan}"

    def make_sound(self):
        print(f"{self.name} клекочет.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self):
        return f"Млекопитающее: {super().__str__()}, цвет шерсти: {self.fur_color}"

    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def __str__(self):
        return f"Рептилия: {super().__str__()}, среда обитания: {self.habitat}"

    def make_sound(self):
        print(f"{self.name} шипит.")

# 3. Демонстрация полиморфизма

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# 4. Использование композиции для создания класса Zoo

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} поставлен на учет в зоопарке.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} принят на работу в зоопарк.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке сохранена в файл {filename}.")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
            print(f"Информация о зоопарке загружена из файла {filename}.")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создается новый зоопарк.")
            return Zoo()

# 5. Создание классов для сотрудников

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} ухаживает за обитателем зоопарка '{animal.name}'.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит обитателя зоопарка '{animal.name}'.")

# Тестирование кода

# Загрузка зоопарка из файла или создание нового
zoo = Zoo.load_from_file('zoo_data.pkl')

# Создание животных
sparrow = Bird("Орел", 9, "188 см")
lion = Mammal("Лев", 8, "Бежевый")
snake = Reptile("Питон", 13, "Восточная Азия")

# Добавление животных (если они не добавлены ранее)
if not any(animal.name == sparrow.name for animal in zoo.animals):
    zoo.add_animal(sparrow)

if not any(animal.name == lion.name for animal in zoo.animals):
    zoo.add_animal(lion)

if not any(animal.name == snake.name for animal in zoo.animals):
    zoo.add_animal(snake)

# Вывод всех сведений о животных
print(sparrow)
print(lion)
print(snake)

# Создание сотрудников
zookeeper = ZooKeeper("Максим Сухов")
veterinarian = Veterinarian("Антон Попов")

# Добавление сотрудников (если они не добавлены ранее)
if not any(staff.name == zookeeper.name for staff in zoo.staff):
    zoo.add_staff(zookeeper)

if not any(staff.name == veterinarian.name for staff in zoo.staff):
    zoo.add_staff(veterinarian)

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(sparrow)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Использование методов сотрудников
zookeeper.feed_animal(lion)
veterinarian.heal_animal(snake)

# Сохранение зоопарка в файл
zoo.save_to_file('zoo_data.pkl')
