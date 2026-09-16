from typing import Any

class Node:
    def __init__(self, val : Any) -> None:
        self.val = val 
        self.next : None | Node = None


class linkedList():
    def __init__(self):
        self.head : Node = Node(None)

    def __iter__(self):
        self.current_node : Node | None = self.head
        while self.current_node != None:
            yield self.current_node
            self.current_node = self.current_node.next


