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
            while last.next:
                last=last.next
            last.next=new_node
        
        for i in l2:
            new_node=ListNode(i)
            
            while last.next:
                last=last.next
            last.next=new_node
        
        return ans.next
​
# aisa dimag bhi laga liya kar bhai!!!!
#def partition(self, head, x):
#    h1 = l1 = ListNode(0)
#    h2 = l2 = ListNode(0)
#    while head:
#        if head.val < x:
#            l1.next = head
#            l1 = l1.next
#        else:
#           l2.next = head
#           l2 = l2.next
#        head = head.next
#    l2.next = None
#    l1.next = h2.next
#    return h1.next
