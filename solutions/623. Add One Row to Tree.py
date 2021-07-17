            d=self.maxDepth(root)
            print(d)
            if depth>d:
                self.deepestNode(root,val,d)
            else:
                self.creator(root,1,val,depth)
            return root
    
    def deepestNode(self,root,val,d):
        if not root:
            return
        if d==1:
            root.left=TreeNode(val)
            root.right=TreeNode(val)
        elif d>1:
            self.deepestNode(root.left,val,d-1)
            self.deepestNode(root.right,val,d-1)
    
    def creator(self,root,t,val,depth):
        if not root:
            return
        elif t==depth-1:
            #if root.left and root.right:
                temp=root.left
                root.left=TreeNode(val)
                root.left.left=temp
                temp=root.right
                root.right=TreeNode(val)
                root.right.right=temp
                #t+=1
            #elif root.left and not root.right:
            #    temp=root.left
            #    root.left=TreeNode(val)
            #    root.left.left=temp
            #elif not root.left and root.right:
            #    temp=root.right
            #    root.right=TreeNode(val)
            #    root.right.right=temp
            #elif root.left
            #print(root.val)
        else:
            self.creator(root.left,t+1,val,depth)
            self.creator(root.right,t+1,val,depth)
    
    def maxDepth(self,root):
        if root is None:
            return 0
        else:
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)
            return 1+max(left,right)
