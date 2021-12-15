from typing import ClassVar
from typing_extensions import Self


class Dog:
    name = "코코"
    age = 2

    def bark(self):
        print('멍멍')

    def move(self):
        print('움직인다.')

dog1 = Dog()

dog1.bark()
print(type(dog1))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('멍멍')

    def move(self):
        print('움직인다.')

    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence

dog1 = Dog('코코' , 2)
dog2 = Dog('두리', 4)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

class Animal:
    def eat(self): 
        print('먹는다')
    
    def move(self):
        print('움직인다')

class Dog (Animal):
    def bark(self): 
        print('멍멍')
    
    def shake(self):
        print('꼬리를 흔든다')

dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()


class Animal:
    def __init__(self, name, age, owner): 
        Self.name = name
        Self.owner = owner 

        
    def eat(self): 
        print('먹는다')

    def move(self):
        print('움직인다')

class Dog (Animal):
    def eat(self): 
        print('먹는다')
    
    def move(self):
        print('움직인다')
