from __future__ import annotations
from ..Unit.Unit import Unit
from ..Battle.Battle import Battle
import random

class Army:
    
    # Initializes the amount of gold available for an Army once it was created
    def __init__(self, units: list[Unit]):
        self._gold = 1000
        if len(units) == 0:
            raise Exception("The army needs at least one unit to be created")
        self._units = units
        self._battles = []
        
    # Tries to train the unit given as a parameter with the current amount of gold.
    # If the amount of gold is enough to accomplish the training, the amount of gold
    # is updated.
    # If there's not enough gold to train the unit, nothing happens.
    def train(self, unit: Unit):
        self._checkUnit(unit)
        remaining = unit.train(self._gold)
        self._gold = remaining
    
    # Tries to transform the unit given as a parameter with the current amount of gold.
    # If the amount of gold is enough to accomplish the transformation, the amount of gold
    # is updated.
    # If there's not enough gold to transform the unit, nothing happens.
    def transform(self, unit: Unit):
        self._checkUnit(unit)
        remaining = unit.transform(self._gold)
        self._gold = remaining
    
    # Checks if the unit is valid and belongs to this Army
    def _checkUnit(self, unit: Unit):
        if unit == None:
            raise ValueError("The unit is not valid")
        if unit not in self._units:
            raise ValueError("The unit does not belong to the army")
    
    # Updates the state of this army and the army given as an argument considering that they 
    # went into battle.
    def attack(self, otherArmy: Army):
        if otherArmy is None:
            raise ValueError("The army is not valid")
        
        if otherArmy is self:
            raise ValueError("The army cannot attack itself")
        
        if len(self._units) == 0:
            raise ValueError("It's not possible to attack an army without units")
        
        if len(otherArmy.getUnits()) == 0:
            raise ValueError("It's not possible to attack an empty army")
        
        selfPoints = self.getPoints()
        otherPoints = otherArmy.getPoints()
        battle = None
        
        if selfPoints > otherPoints:
            self._winBattle()
            otherArmy._loseBattle()
            battle = Battle(self, otherArmy, self)
        elif selfPoints < otherPoints:
            self._loseBattle()
            otherArmy._winBattle()
            battle = Battle(self, otherArmy, otherArmy)           
        else:
            self._drawBattle()
            otherArmy._drawBattle()
            battle = Battle(self, otherArmy, None)
        
        self.addBattle(battle)
        otherArmy.addBattle(battle)
    
    # Updates the state of the army considering that it won a battle.
    def _winBattle(self):
        self._gold += 100
    
    # Updates the state of the army considering that it draw a battle.
    # CRITERIA: when an army draws a battle, I defined as criteria that it will loose its worst unit
    def _drawBattle(self):
        worstUnit = self._units[0]
        for i in range(1, len(self._units)):
            if worstUnit.getPoints() > self._units[i].getPoints():
                worstUnit = self._units[i]
                
        self._units.remove(worstUnit)
        return
    
    # Updates the state of the army considering that it lose a battle 
    def _loseBattle(self):
        bestUnit = self._getBestUnit()
        if (bestUnit != None):
            self._units.remove(bestUnit)
        
        bestUnit = self._getBestUnit()
        if (bestUnit != None):
            self._units.remove(bestUnit)
    
    # Adds a new battle to the army's history of battles
    def addBattle(self, battle: Battle):
        if (self is not battle.firstArmy() and self is not battle.secondArmy()):
            raise ValueError("The battle cannot belong to this army")
        self._battles.append(battle)
    
    # Returns the amount of points represented by the units that are part of the army 
    def getPoints(self):
        points = 0
        for i in range(0, len(self._units)):
            points += self._units[i].getPoints()
        return points
    
    # Returns the list of units that belong to the army
    def getUnits(self) -> list[Unit]:
        return self._units
    
    # Returns the best unit in the army
    def _getBestUnit(self):
        if len(self._units) == 0:
            return None
        bestUnit = self._units[0]
        for i in range(1, len(self._units)):
            if bestUnit.getPoints() < self._units[i].getPoints():
                bestUnit = self._units[i]
                
        return bestUnit