class Animal:
    alive = True #живой
    fed = False #накормленный
    def __init__(self, name):
        self.name = name

class Plant:
    adible = False #съедобный
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        self.food = Plant(self.name)
        if self.food == False:
            fed = True
            print(f'{self.name} съел {food.name}')
        else:
            alive = False
            print(f'{self.name} не стал есть {food.name}')
class Predator(Animal):
   def eat(self, food):
        self.food = Plant(self.name)
        if self.food == False:
            fed = True
            print(f'{self.name} съел {food.name}')
        else:
            alive = False
            print(f'{self.name} не стал есть {food.name}')
class Flower(Plant):
    edible = True
class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)