from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component():
    '''
    base component interface that defines an operation which can be altered by a decorator
    '''

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    '''
    the concrete component that has a default implementation of an operation. Could be several of these classes.
    '''

    def operation(self) -> str:
        return 'concrete component'


class Decorator(Component):
    '''
    This would be the abstract decorator class that concrete decorator classes would use
    '''

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    ''' here a concrete decorator class does the actual decoration around a component'''
    def operation(self) -> str:
        return f'ConcreteDecoratorA({self.component.operation()})'


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f'ConcreteDecoratorB({self.component.operation()})'


if __name__ == '__main__':
    simple = ConcreteComponent()
    print(simple.operation())

    a = ConcreteDecoratorA(simple)
    print(a.operation())
    b = ConcreteDecoratorB(a)
    print(b.operation())

    quit()
