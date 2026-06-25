import sys
from ex0.factories import CreatureFactory
from ex2.strategies import BattleStrategy, InvalidStrategyError


class Tournament:
    def __init__(
            self, oponents: list[tuple[CreatureFactory, BattleStrategy]]
            ) -> None:
        self.opponents: list[tuple[CreatureFactory, BattleStrategy]] = oponents

    def execute(self) -> None:
        print("*** Tournament ***")
        print(f"{len(self.opponents)} opponents involved")

        if not self.opponents:
            return

        for i in range(len(self.opponents)):
            for j in range(i + 1, len(self.opponents)):
                fact_1, strat_1 = self.opponents[i]
                fact_2, strat_2 = self.opponents[j]

                c1 = fact_1.create_base()
                c2 = fact_2.create_base()

                print(" * Battle *")
                print(f"{c1.describe()}")
                print(" vs.")
                print(f"{c2.describe()}")
                print(" now fight!")

                try:
                    logs_1 = strat_1.act(c1)
                    for log in logs_1:
                        print(log)
                except InvalidStrategyError as e:
                    print(f"Battle error, aborting tournament: {e}")
                    sys.exit(1)

                try:
                    logs_2 = strat_2.act(c2)
                    for log in logs_2:
                        print(log)
                except InvalidStrategyError as e:
                    print(f"Battle error, aborting tournament: {e}")
                    sys.exit(1)
