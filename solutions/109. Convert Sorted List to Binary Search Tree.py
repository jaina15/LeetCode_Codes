# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    #this part is done by storing linkedlist into an array and then created the tree
    #    a=[]
    #    temp=head
    #    while temp:
    #        a.append(temp.val)
    #        temp=temp.next
    #    
    #    root=self.creator(a)
    #    return root
    #
    #def creator(self,a):
    #    if not a:
    #        return
    #    mid=len(a)//2
    #    root=TreeNode(a[mid])
    #    
    #    root.left=self.creator(a[:mid])
    #    root.right=self.creator(a[mid+1:])
    #    return root
    
    #using linked list only
        root=self.creator(head)
        return root
        
    def creator(self,head):
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        temp=head
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        #print(prev)
        if prev:
            prev.next=None
        #print(temp)
        #print(slow)
        root=TreeNode(slow.val)
        root.left=self.creator(temp)
        root.right=self.creator(slow.next)
        #print('root',root.val)
        return root
