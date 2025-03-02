class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    all = []
    def __init__(self, name, pet_type, owner=None): # type: ignore
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        Pet.all.append(self)
        
    pass

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    pass
    
    def add_pet(self, pet):
        pet.owner = self
    pass
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass
    
    def owner_has_pets(self):
        return len(self.pets()) > 0
    pass



    
