from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()

    print("base: ")
    h_base = heal_factory.create_base()
    print(h_base.describe())
    print(h_base.attack())
    if isinstance(h_base, HealCapability):
        print(h_base.heal())

    print("evolved: ")
    h_evolved = heal_factory.create_evolved()
    print(h_evolved.describe())
    print(h_evolved.attack())
    if isinstance(h_evolved, HealCapability):
        print(h_evolved.heal())

    print("\nTesting Creature with transform capability")
    trans_factory = TransformCreatureFactory()

    print("base: ")
    t_base = trans_factory.create_base()
    print(t_base.describe())
    print(t_base.attack())
    if isinstance(t_base, TransformCapability):
        print(t_base.transform())
        print(t_base.attack())
        print(t_base.revert())

    print("evolved: ")
    t_evolved = trans_factory.create_evolved()
    print(t_evolved.describe())
    print(t_evolved.attack())
    if isinstance(t_evolved, TransformCapability):
        print(t_evolved.transform())
        print(t_evolved.attack())
        print(t_evolved.revert())
