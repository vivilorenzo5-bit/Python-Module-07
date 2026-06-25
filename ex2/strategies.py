from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    ...


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AgressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if isinstance(creature, TransformCapability):
            logs = []
            logs.append(creature.transform())
            logs.append(creature.attack())
            logs.append(creature.revert())
            return logs
        raise InvalidStrategyError(
            f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if isinstance(creature, HealCapability):
            logs = []
            logs.append(creature.attack())
            logs.append(creature.heal())
            return logs
        raise InvalidStrategyError(
            f"Invalid Creature '{creature.name}' for this defensive strategy"
        )
