class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def eat(self):
        print('{}가 먹는다'.format(self.name))

    def move(self):
        print('움직인다')   

class Dog (Animal):
    def __init__(self, name, age, owner):
        super(). __init__(name, age)
        self.owner = owner

    def bark(self):
        print('멍멍')

    def shake(self):
        print('{}가 꼬리를 흔든다'.format(self.name)) 

    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age, self.owner)
        return sentence

dog = Dog('코코', 2, '홍길동')
print(dog)
dog.shake()
dog.bark()
dog.eat()
dog.move()

dog = Dog('두식이', 1, '친구')
print(dog)
dog.shake()
dog.eat()

class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def eat(self):
        print('{}가 먹는다'.format(self.name))

    def move(self):
        print('움직인다')   

class Dog(Animal):
    def __init__(self, name, age, owner):
        super(). __init__(name, age)
        self.owner = owner

    def bark(self):
        print('멍멍')

    def shake(self):
        print('{}가 꼬리를 흔든다'.format(self.name)) 

    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age, self.owner)
        return sentence


dog = Dog('두리', 5, '홍길동')
print(dog)
dog = Dog('먼지', 7, '홍길동')
print(dog)
dog = Dog('두식', 7, '친구')
print(dog)

class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def eat(self):
        print('{}가 먹는다'.format(self.name))

    def move(self):
        print('움직인다')   

class Dog(Animal):
    def __init__(self, name, age, owner):
        super(). __init__(name, age)
        self.owner = owner

    def bark(self):
        print('멍멍')

    def shake(self):
        print('{}가 꼬리를 흔든다'.format(self.name)) 

    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age, self.owner)
        return sentence

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def eat(self):
        print('새가 모이를 먹는다')

    def move(self):
        print('새가 몸을 움직인다')

    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence

animal = Animal('',0)
animal.eat()
animal.move()

dog = Dog('코코', 2,'')
print(dog)
dog.eat()
dog.move()

bird = Bird('먼지', 2)
print(bird)
bird.eat()
bird.move()
