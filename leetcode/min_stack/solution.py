class Node:
    def __init__(self, val=0, min_so_far=float('inf')):
        self.val = val
        self.min_so_far = min_so_far
        self.next = None

class MinStack:
    def __init__(self):
        self.dummy = Node()

    def push(self, val: int) -> None:
        if not self.dummy.next:
            self.dummy.next = Node(
                val,
                min(val, val)
            )
        else:
            tmp = self.dummy.next
            new_node = Node(
                val,
                min(val, tmp.min_so_far)
            )
            new_node.next = tmp
            self.dummy.next = new_node

    def pop(self) -> None:
        self.dummy.next = self.dummy.next.next

    def top(self) -> int:
        return self.dummy.next.val

    def getMin(self) -> int:
        return self.dummy.next.min_so_far

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()