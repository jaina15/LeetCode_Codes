from collections import deque
class MyStack:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=deque()
        
​
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        z=deque([x])
        z.extend(self.q)
        self.q=z
        
        
​
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()
        
​
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]
        
        
​
