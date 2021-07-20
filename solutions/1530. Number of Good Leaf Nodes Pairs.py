# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# i am getting TLE with this approach. Will try this in revision time to optmize it and get it passed.
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance==1 and (root.left or root.right):
            return 0
        #if dist==1 and not root.left and not root.right:
        #    return 1
        leaf_nodes=[]
        ans=0
        self.inorder(root,leaf_nodes)
        #print(leaf_nodes)
        
        for i in range(len(leaf_nodes)-1):
            for j in range(i+1,len(leaf_nodes)):
                lca=self.lca(root,leaf_nodes[i],leaf_nodes[j])
                #print(lca.val,leaf_nodes[i].val,leaf_nodes[j].val)
                #print(self.finddepth(lca,leaf_nodes[i]))
                #print(self.finddepth(lca,leaf_nodes[j]))
                if self.finddepth(lca,leaf_nodes[i])+self.finddepth(lca,leaf_nodes[j])<=distance:
                    ans+=1
        return ans
        
    def inorder(self,root,leaf_nodes):
        if root:
            self.inorder(root.left,leaf_nodes)
            if not root.left and not root.right:
                leaf_nodes.append(root)
            self.inorder(root.right,leaf_nodes)
    
    def lca(self,root,p,q):
        if not root:
            return
        if root==p or root==q:
            return root
        l=self.lca(root.left,p,q)
        r=self.lca(root.right,p,q)
        if l and r:
            return root
        if not l and not r:
            return None
        return l if l is not None else r
    
    def finddepth(self,root,x):
        if not root:
            return -1
        dist=-1
        if root==x:
            return dist+1
        
        dist = self.finddepth(root.left, x)
        if dist >= 0:
            return dist + 1
        dist = self.finddepth(root.right, x)
        if dist >= 0:
            return dist + 1
        return dist
