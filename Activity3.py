class Parrot:
    def __init__(self,name,age,species = "bird"):
        self.name = name
        self.age = age
        self.species = species
blue = Parrot("blue",10)
parakeet = Parrot("parakeet",10)
print(blue.species,blue.name,blue.age)
print(parakeet.species,parakeet.name,parakeet.age)
        