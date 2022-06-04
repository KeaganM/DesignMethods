from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self,strategy:Strategy) -> None:
        self._strategy = strategy

    def run_strategy(self,*args,**kwargs) -> None:
        return self._strategy.run(*args,**kwargs)



class Strategy(ABC):
    @abstractmethod
    def run(self,*args,**kwargs):
        raise NotImplementedError

class ConcretStrategySorting(Strategy):
    def run(self,string:str):
        return ''.join(sorted(string))


class ConcretStrategyReverse(Strategy):
    def run(self,string:str):
        return ''.join(list(reversed(string)))


if __name__ == '__main__':

    string = 'a green apple'

    context = Context(ConcretStrategySorting())
    result = context.run_strategy(string)
    print(result)

    context.strategy = ConcretStrategyReverse()
    result = context.run_strategy(string)
    print(result)



    quit()
