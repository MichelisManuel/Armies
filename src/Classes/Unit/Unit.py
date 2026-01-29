from ..Role.Role import Role

class Unit:
    
    def __init__(self, age: int, role: Role):
        self._age = age
        self._role = role
        self._strengthPoints = role.getBaseStrengthPoints()
        
    # Returns the corresponding age of the unit
    def getAge(self):
        return self._age
    
    # Tries to train itself depending on his role, using the amount of gold passed as argument.
    # Returns the remaining amount of gold after training the unit, if it's possible to do it.
    # If it's not, returns the amount of gold passed as argument
    def train(self, gold: int):
        remaining, strengthPoints = self._role.train(gold)
        self._strengthPoints += strengthPoints
        return remaining
    
    # Tries to transform itself depending on his role, using the amount of gold passed as argument.
    # Returns the remaining amount of gold after transform the unit and the new Role object, if it's possible to do it.
    # If it's not, returns the amount of gold passed as argument and the current Role object
    def transform(self, gold: int):
        # The transformation can be done, so I have to update the corresponding amount of gold and the Role itself
        remaining, self._role = self._role.transform(gold)
        self._strengthPoints = self._role.getBaseStrengthPoints()
        return remaining
    
    # Returns the amount of strength points that the unit has
    def getPoints(self) -> int:
        return self._strengthPoints