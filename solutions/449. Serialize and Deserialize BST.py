# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
​
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        l=[]
        self.preorder(root,l)
        print(l)
        s=''
        for i in l:
            s+=str(i)+' '
        print(s)
        return s
    
    def preorder(self,root,l):
        if root:
            l.append(root.val)
            #l+=str(root.val)+' '
            self.preorder(root.left,l)
            self.preorder(root.right,l)
        
​
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data)==0:
            return
        l=[]
        s=''
        root=TreeNode(None)
        for i in data:
            if i!=' ':
                s+=i
            else:
                l.append(s)
                self.insert(root,int(s))
                s=''
        print(l)
        return root
    
    def insert(self,root,data):
        if root.val is None:
            root.val=data
            return
        if root.val>data:
            if root.left:
                self.insert(root.left,data)
            else:
                root.left=TreeNode(data)
        else:
            if root.right:
                self.insert(root.right,data)
            else:
                root.right=TreeNode(data)
            
        
​
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
