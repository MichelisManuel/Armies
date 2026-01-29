from abc import ABC, abstractmethod

class Role(ABC):
    
    def __init__(self):
        super().__init__()
    
    # Trains the role with the amount of gold given as an argument, if it's possible, and returns the remaining
    # amount of gold.
    # If it's not possible, it returns the amount of gold given as an argument
    @abstractmethod
    def train(self, gold: int):
        pass
    
    # Transforms the role with the amount of gold given as an argument, if it's possible, and returns the remaining
    # amount of gold and the new Role object.
    # If it's not possible, it returns the amount of gold given as an argument and the self Role object
    @abstractmethod
    def transform(self, gold: int):
        pass
    
    # Returns the amount of basic strength points that the specific role has
    @abstractmethod
    def getBaseStrengthPoints(self) -> int:
        pass
    
    # Determines if the role can be transformed with the amount of gold given as an argument
    @abstractmethod
    def canBeTransformed(self, gold: int) -> bool:
        pass