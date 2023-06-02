import random


class Tyrannosaurus:
    def __init__(self, name):
        self.name = name

    def roar(self):
        print(f"{self.name} реве!")

    def hunt(self, target):
        print(f"{self.name} полює на {target}!")


class Triceratops:
    def __init__(self, name):
        self.name = name

    def charge(self):
        print(f"{self.name} налетів!")

    def graze(self):
        print(f"{self.name} пасеться!")



tyrannosaurus = Tyrannosaurus("Тиранозавр Рекс")
triceratops = Triceratops("Трицератопс Хорн")


user_chance = int(input("Введіть свій шанс (від 1 до 10): "))


if 1 <= user_chance <= 5:
    tyrannosaurus.roar()
    tyrannosaurus.hunt("трицератопса")
else:
    triceratops.charge()
    triceratops.graze()
