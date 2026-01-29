from Classes.Unit.Unit import Unit
from Classes.Army.Army import Army
from Classes.Battle.Battle import Battle
from Classes.Role.Pikeman import Pikeman
from Classes.Role.Archer import Archer
from Classes.Role.Knight import Knight

pikeman1 = Unit(30, Pikeman())
archer1 = Unit(30, Archer())
knight1 = Unit(30, Knight())

pikeman2 = Unit(30, Pikeman())
archer2 = Unit(30, Archer())
knight2 = Unit(30, Knight())

army1: Army = Army([pikeman1, archer1, knight1])
army2: Army = Army([pikeman2, archer2, knight2])

print("Army 1 starts with ", len(army1.getUnits()), "units and ", army1.getPoints(), " points")
print("Army 2 starts with ", len(army2.getUnits()), "units and ", army2.getPoints(), " points")
print("----------------------------------------")
print("Army 1 attacks Army 2!")
army1.attack(army2)
print("Army 1 points:", army1.getPoints())
print("Army 2 points:", army2.getPoints())
print("Army 1 units:", len(army1.getUnits()))
print("Army 2 units:", len(army2.getUnits()))
print("----------------------------------------")
print("Army 1 attacks Army 2!")
army1.attack(army2)
print("Army 1 points:", army1.getPoints())
print("Army 2 points:", army2.getPoints())
print("Army 1 units:", len(army1.getUnits()))
print("Army 2 units:", len(army2.getUnits()))
