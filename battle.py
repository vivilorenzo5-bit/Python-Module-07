from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    print("\nTesting battle")
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print(creature_a.describe())
    print(" VS.")
    print(creature_b.describe())
    print("fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()

    test_factory(flame_fact)
    print("")
    test_factory(aqua_fact)

    test_battle(flame_fact, aqua_fact)
