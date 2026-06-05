# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'некое животное'
    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'птица'
    def make_sound(self):
        print('курлык-курлык')
    def eat(self):
        print(f'{self.name} клюет зерно')

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'млекопитающее'
    def make_sound(self):
        print('рычит')
    def eat(self):
        print(f'{self.name} пережевывает еду')

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'рептилия'
    def make_sound(self):
        print('шипит')
    def eat(self):
        print(f'{self.name} проглатывает')

class ZooKeeper():
    def __init__(self, name):
        self.name = name
        self.prof = "Смотритель"
    def feed_animal(self, animal):
        print(f'{self.name} покормил {animal.name}')
    def pet_animal(self, animal):
        print(f'{self.name} погладил {animal.name}')

class Veterinarian():
    def __init__(self, name):
        self.name = name
        self.prof = "Ветеринар"
    def heal_animal(self, animal):
        print(f'{self.name} полечил {animal.name}')
    def regen_animal(self, animal):
        print(f'{self.name} наложил реген на {animal.name}')

class Zoo():
    def __init__(self, name):
        self.name = name
        self.list_workers = []
        self.list_animals = []
    def add_worker(self, worker):
        rele = True
        for i in self.list_workers:
            if i.name == worker.name:
                print('Работник с таким именем уже есть.')
                rele = False
                break
        if rele:
            self.list_workers.append(worker)
    def add_animal(self, animal):
        rele = True
        for i in self.list_animals:
            if i.name == animal.name:
                print('Животное с таким именем уже есть.')
                rele = False
                break
        if rele:
            self.list_animals.append(animal)

    def show_list_workers(self):
        print(f'Сотрудники зоопарка \"{self.name}\":')
        for i, worker in enumerate(self.list_workers, start=1):
            print(f'{i}. {worker.name} - {worker.prof}')
    def show_list_animals(self):
        print(f'Животные зоопарка \"{self.name}\":')
        for i, animal in enumerate(self.list_animals, start=1):
            print(f'{i}. {animal.name} - {animal.type}, возраст: {animal.age}')

    def delete_animal(self, animal):
        rele = True
        for i in self.list_animals:
            if i.name == animal:
                self.list_animals.remove(i)
                rele = False
                break
        if rele:
            print('Нет животного с таким именем')
    def delete_worker(self, worker):
        rele = True
        for i in self.list_workers:
            if i.name == worker:
                self.list_workers.remove(i)
                rele = False
                break
        if rele:
            print('Нет работника с таким именем.')


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

ivan = ZooKeeper("Ivan")
semen = Veterinarian('Semen')
croc = Reptile("Sam", 2)
kesha = Bird("Kesha", 4)
murka = Mammal("Murka", 11)

nj = Zoo("Зоопарк имени Неуловимого Джо")
nj.add_animal(croc)
nj.add_animal(kesha)
nj.add_animal(murka)
nj.add_worker(ivan)
nj.add_worker(semen)
nj.show_list_animals()
nj.show_list_workers()

croc.eat()
ivan.pet_animal(kesha)
kesha.make_sound()
semen.regen_animal(ivan)

nj.add_worker(Veterinarian('Kolya'))
nj.add_animal(Reptile('Snake Tom', 2))
nj.delete_animal("Sam")
nj.delete_worker('Semen')
nj.delete_worker('Murka')
nj.show_list_animals()
nj.show_list_workers()

animal_sound(nj.list_animals)
