from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..Army.Army import Army

class Battle:
    
    # Initializes the battle with the involved armies and the winner army, if exists
    def __init__(self, firstArmy: Army, secondArmy: Army, winner: Army):
        if winner is not firstArmy and winner is not secondArmy and winner is not None:
            raise ValueError("The winner army has to be either the first army, second army or none")
        self._firstArmy = firstArmy
        self._secondArmy = secondArmy
        self._winner = winner
    
    # Returns the first army involved in the battle  
    def firstArmy(self):
        return self._firstArmy
    
    # Returns the second army involved in the battle  
    def secondArmy(self):
        return self._secondArmy