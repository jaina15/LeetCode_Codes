# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
​
    def __init__(self, root: TreeNode):
        self.root=root
        self.x=0
        self.l=[]
        self.preorder(self.root,self.x,self.l)
    
    def preorder(self,root,x,l):
        if root:
            root.val=x
            l.append(root.val)
            if root.left:
                self.preorder(root.left,(2*root.val+1),l)
            if root.right:
                self.preorder(root.right,(2*root.val+2),l)
​
    def find(self, target: int) -> bool:
        if target in self.l:
            return True
        return False
​
​
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
