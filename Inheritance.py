class Mammal:
    def walk(self):
        print("walk")

class Bat(Mammal):
    pass

class Fish(Mammal):
    pass

class Penguin(Mammal):
    pass


animal1=Bat()
animal1.walk()

animal2=Fish()
animal2.walk()

animal3=Penguin()
animal3.walk()