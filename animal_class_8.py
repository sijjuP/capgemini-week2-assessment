class Animal:
    def speak(self):
        print("\nAnimal makes sound\n")

class Dog(Animal):
    def speak(self):
        print("\nDog Barks\n")

class Cat(Animal):
    def speak(self):
        print("\nCat meows\n")

cat_obj=Cat()
dog_obj=Dog()
animal_obj=Animal()

animal_obj.speak()
cat_obj.speak()
dog_obj.speak()

