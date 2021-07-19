# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: TreeNode):
        self.root=root
        self.l=[]
        self.inorder(root,self.l)
        self.i=0
    
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
​
    def next(self) -> int:
        ans=self.l[self.i]
        self.i+=1
        return ans
​
    def hasNext(self) -> bool:
        if self.i<len(self.l):
            return True
        return False
​
​
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
