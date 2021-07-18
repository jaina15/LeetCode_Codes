    
    def check(self,head,root):
        if not head:
            return True
        if not root:
            return False
        if head.val==root.val:
            return self.check(head.next,root.left) or self.check(head.next,root.right)
        
''' isse hogya but complexity zyada h
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        list_path=''
        while head:
            list_path+=str(head.val)+' '
            head=head.next
        l=[]
        s=''
        self.creator(root,l,s)
        for i in range(len(l)):
            if list_path in l[i]:
                return True
        
        return False
    
    def creator(self,root,l,s):
        if root is None:
            return
        
        s+=str(root.val)+' '
​
        if root.left is None and root.right is None:
            l.append(s)
        self.creator(root.left,l,s)
        self.creator(root.right,l,s)
​
'''
    
''' 65/67 p fatt rha h
    ans=False
    temp=None
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.temp=head
        self.preorder(head,root)
        return self.ans
    
    def preorder(self,head,root):
        if root and head:
            if root.val==head.val:
                self.temp=head
                self.preorder(head.next,root.left)
                self.preorder(head.next,root.right)
                if head.next is None or head is None:
                    self.ans=True
            else:
                head=self.temp
                if head.val==root.val:
                    self.preorder(head,root)
                else:
                    self.preorder(head,root.left)
                    self.preorder(head,root.right)
'''
