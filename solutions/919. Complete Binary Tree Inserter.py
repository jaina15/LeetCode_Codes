# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class CBTInserter:
​
    def __init__(self, root: TreeNode):
        self.root=root
​
    def insert(self, v: int) -> int:
        if not self.root:
            return TreeNode(v)
        q=queue()
        q.append(self.root)
        while q:
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
            else:
                curr.left=TreeNode(v)
                return curr.val
            if curr.right:
                q.append(curr.right)
            else:
                curr.right=TreeNode(v)
                return curr.val
        
​
    def get_root(self) -> TreeNode:
        return self.root
​
​
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
