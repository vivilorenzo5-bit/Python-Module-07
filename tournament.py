from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    Tournament, NormalStrategy, AggressiveStrategy, DefensiveStrategy
)


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    opponents_0 = [
        (flame_f, NormalStrategy()),
        (heal_f, DefensiveStrategy())
    ]
    t0 = Tournament(opponents_0)
    t0.execute()
    print()

    print("Tournament 1 (error)")
    opponents_1 = [
        (flame_f, AggressiveStrategy()),
        (heal_f, DefensiveStrategy())
    ]
    t1 = Tournament(opponents_1)
    t1.execute()
    print()

    print("Tournament 2 (multiple)")
    opponents_2 = [
        (aqua_f, NormalStrategy()),
        (heal_f, DefensiveStrategy()),
        (trans_f, AggressiveStrategy())
    ]
    t2 = Tournament(opponents_2)
    t2.execute()
