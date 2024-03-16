#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name ="dog joe", breed = "Pointer"):
        self.name = name
        self.breed = breed

    # name
    @property
    def name(self):        
        return self._name
    @name.setter
    def name(self,name): 
        if(type(name) is str and ( 0 < len(name) < 26 ) ):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    # breed 
    @property   
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed_name):
        if(breed_name in APPROVED_BREEDS):            
            self._breed = breed_name
        else:
            print("Breed must be in list of approved breeds.")

    

