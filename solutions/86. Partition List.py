# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1=[]
        l2=[]
        
        temp=head
        while temp:
            if temp.val<x:
                l1.append(temp.val)
                #temp=temp.next
            else:
                l2.append(temp.val)
            temp=temp.next
        
        if len(l1)>=1 and len(l2)==0:
            return head
        if len(l1)==0 and len(l2)>=1:
            return head
        
        #print(l1)
        #print(l2)
        new_head=ListNode(0)
        ans=new_head
        last=None
        for i in l1:
            new_node=ListNode(i)
            
            last=new_head
