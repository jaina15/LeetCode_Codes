# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #using bfs to find parent and storing in a 2d list
        if root is None:
            return False
        q=queue()
        q.append(root)
        l=[]
        while len(q)>0:
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
                if curr.left.val==x:
                    l.append([x,curr.val])
                elif curr.left.val==y:
                    l.append([y,curr.val])
            if curr.right:
                q.append(curr.right)
                if curr.right.val==x:
                    l.append([x,curr.val])
                elif curr.right.val==y:
                    l.append([y,curr.val])
            
            if len(l)==2:
                break
        #print(l)
        depth_x=self.depth(root,x)
        depth_y=self.depth(root,y)
        #print(depth_x,depth_y)
        if depth_x==depth_y and l[0][1]!=l[1][1]:
            return True
        return False
    
    def depth(self,root,x):
        if root is None:
            return -1
        
        dist=-1
        if root.val==x:
            return dist+1
        dist=self.depth(root.left,x)
        if dist>=0:
            return dist+1
        dist=self.depth(root.right,x)
        if dist>=0:
            return dist+1
        return dist
