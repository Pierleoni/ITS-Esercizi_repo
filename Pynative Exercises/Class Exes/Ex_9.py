class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

def main():
    
    print(f"Dog is a sublclass of Animal? → {issubclass(Dog, Animal)}\n")
    print (f"Animal is a subclass of Dog? → {issubclass(Animal, Dog)}\n")
    print(f"Cat is a sublclass of Animal? → {issubclass(Cat, Animal)}\n")

    print(f"Puppy is subclass of Animal? → {issubclass(Puppy, Animal)}")

if __name__ == "__main__":
    main()