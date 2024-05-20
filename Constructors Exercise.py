class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"My name is {self.name}")

str1=input("Enter Your Name: ")
p1 = Person(str1)
print(p1.name)
p1.talk()
