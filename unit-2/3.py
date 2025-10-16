class Animal:
    def make_sound(self):
        print("Sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    def make_sound(self):
        print("Chirp")

Dog().make_sound()
Cat().make_sound()
Bird().make_sound()
