# Composite Pattern

## Index

- [Type](#Type)
- [Summary](#Summary)
- [Usage](#Usage)
- [Boilerplate](#Boilerplate)
- [Example(s)](#Examples)
- [Consequences](#Consequences)
- [Implementation](#Implementation)
- [Resources](#Resources)

## Type

- Structural

## Summary

- Allow for additional responsibility to be applied to an object dynamically. This is done by essentially wrapping an
  object with additional functionality. Also known as a wrapper.
- Essentially forwarding requests to the object in question but may do something before or after the request gets to the
  object.

## Usage

- when you want to add/remove responsibility to an object dynmically and transparently without affecting other objects
- when extension by subclassing is impossible to too explosive; may be easier to wrap an object with additional
  functionality rather than sublcass it to handle a niche case
![img_1.png](img_1.png)
## BoilerPlate

```python
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

```

## Examples

## Consequences

- more flexibility than static inheritance
    - can add/remove functionality
- pay-as-you-go approach; instead of trying to account for possible desired functionality, you can make a simple class
  and wrap it in extra functionality later
- decorated component is not identical to the component itself; don't rely on object identity when using decorators
- get lots of little objects and only differ in the way they are interconnected.
    - easily customizable but can be hard to learn and debug comming in.

## Implementation

- Decorator object interface should conform to the interface the component the decorator is decorating. For example, above, both the component and decorator have an operations function used to preform some operation.
- Can skip implementing an abstract decorator class if you are only applying a single extra piece of responsibility
- keep component classes lightweight
  - focus on defining an interface rather than storing data
- change the skin not the guts, decorators extend an object's functionality rather than changing things internally
  - components decorated do not need to know or care about the outside decoration
## Resources
- https://refactoring.guru/design-patterns/decorator/python/example