
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []
        self.front : int = -1
        self.rear :  int = -1

    def push(self, item: Any) -> None:
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
        else:
            self.rear += 1
            
        self.items.append(item)
        

    def pop(self) -> Any:
        if len(self.items) == 0:
            return None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return self.items.pop()
        else:
            item : Any = self.items[self.front]
            del self.items[self.front]
            self.rear -= 1
            return item    

    def peek(self) -> Any:
        if self.front == -1:
            return None

        return self.items[self.front]

    def size(self) -> int:
        return len(self.items)
