from ..Role.Role import Role

class Knight(Role):

    TRAINING_COST = 30  
    BASIC_STRENGTH_POINTS = 20  

    # Initializes the strength points for a role of type Knight
    def __init__(self):
        super().__init__()
        self._strengthPoints = 20
    
    def train(self, gold: int):
        if gold >= self.TRAINING_COST:
            # There's enough gold to train this role. I return the remaining amount of gold and the strength points
            return gold - self.TRAINING_COST, 10
        # There's not enoguh gold to train this role. I return the amount of gold passed as argument
        return gold, 0
    
    def transform(self, gold: int):
        return gold, self

    def getBaseStrengthPoints(self):
        return self.BASIC_STRENGTH_POINTS
    
    def canBeTransformed(self, gold: int) -> bool:
        return False