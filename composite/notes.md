# Composite Pattern

## Index

- [Summary](#Summary)
- [Usage](#Usage)
- [Boilerplate](#Boilerplate)
- [Example(s)](#Examples)
- [Consequences](#Consequences)
- [Resources](#Resources)

## Summary

## Usage

## BoilerPlate
```python
from __future__ import annotations  # allows us to reference Component class in the methods in Component
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    @abstractmethod
    def operation(self):
        pass


class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return '\n'.join(results)


class Leaf(Component):
    def operation(self):
        return f'leaf operation'


if __name__ == '__main__':
    branch = Composite()

    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()

    branch.add(leaf1)
    branch.add(leaf2)
    branch.add(leaf3)
    result = branch.operation()
    print(result)

```

## Examples

## Consequences

## Resources
- https://refactoring.guru/design-patterns/composite/python/example