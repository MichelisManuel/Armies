from ..Role.Role import Role
from ..Role.Knight import Knight

class Archer(Role):
    
    TRAINING_COST = 20
    TRANSFORM_COST = 40
    BASIC_STRENGTH_POINTS = 10
    
    # Initializes the strength points for a role of type Archer
    def __init__(self):
        super().__init__()
    
    def train(self, gold: int):
        if gold >= self.TRAINING_COST:
            # There's enough gold to train this role. I return the remaining amount of gold and the strength points
            return gold - self.TRAINING_COST, 7
        # There's not enough gold to train this role. I return the amount of gold passed as argument
        return gold, 0
    
    def transform(self, gold: int):
        if self.canBeTransformed(gold):
            # It can be transformed, so I return the remaining amount of gold after transform the role and the new Role
            return gold - self.TRANSFORM_COST, Knight()
        # There's not enough gold to transform this role. I return the amount of gold passed as argument and the current Role
        return gold, self

    def getBaseStrengthPoints(self):
        return self.BASIC_STRENGTH_POINTS
    
    def canBeTransformed(self, gold: int) -> bool:
        return gold >= 40