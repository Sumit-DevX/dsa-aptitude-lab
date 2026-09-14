
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []
        self.top : int = -1

    def push(self, item: Any) -> None:
        self.top += 1
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        if self.top == -1:
            return None
        return self.items[self.top]

    def pop(self) -> Any:
        if self.top == -1:
            return None
        popped_item : Any = self.items.pop()
        self.top -= 1
        return popped_item
