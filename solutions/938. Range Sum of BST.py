# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #using recursion. ye mene dekha h k recursion kaise use karna h
        #if root is None:
        #    return 0
        #elif root.val<low:
        #    return self.rangeSumBST(root.right,low,high)
        #elif root.val>high:
        #    return self.rangeSumBST(root.left,low,high)
        # 
        #return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
        
        #without recursion using inorder traversal
        l=[]
        self.inorder(root,l)
        print(l)
        ans=0
        for i in l:
            if i>=low and i<=high:
                ans+=i
            if i>high:
                break
        return ans
        
        
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
        
