"""
O Estategy é muito util em cenários onde necessita-se de uma flexibilidade na viração entre classes parecidas que executam comportamentos
diferentes, implementando uma interface intermediadora que mentem a strategy atual e permita sua mudança facilmente.
"""

class Strategy:
    def do_operation(self):
        pass

class ConcreteStrategyA(Strategy):
    def do_operation(self):
        print("Executing operation A")

class ConcreteStrategyB(Strategy):
    def do_operation(self):
        print("Executing operation B")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.do_operation()

# Uso
context = Context(ConcreteStrategyA())
context.execute_strategy()

context = Context(ConcreteStrategyB())
context.execute_strategy()
