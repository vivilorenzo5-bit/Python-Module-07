from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    Tournament, NormalStrategy, AggressiveStrategy, DefensiveStrategy,
    BattleStrategy
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        tournament = Tournament(opponents)
        tournament.execute()
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")


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
    battle(opponents_0)
    print()

    print("Tournament 1 (error)")
    opponents_1 = [
        (flame_f, AggressiveStrategy()),
        (heal_f, DefensiveStrategy())
    ]
    battle(opponents_1)
    print()

    print("Tournament 2 (multiple)")
    opponents_2 = [
        (aqua_f, NormalStrategy()),
        (heal_f, DefensiveStrategy()),
        (trans_f, AggressiveStrategy())
    ]
    battle(opponents_2)
