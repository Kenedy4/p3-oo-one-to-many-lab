class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # This will store the owner's pets

    def pets(self):
        return self._pets  # Return the list of the owner's pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Argument is not a Pet instance")
        
        pet.owner = self  # Set the owner for the pet
        self._pets.append(pet)  # Add the pet to the owner's pet list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Sort pets by their names


# lib/pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet to the owner's pet list if an owner is provided
        if owner:
            owner.add_pet(self)

        Pet.all.append(self)  # Add the current pet instance to the all list

    @classmethod
    def all_pets(cls):
        return cls.all  # Return all instances of the Pet class