# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        slow,fast=head,head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        #print(head)
        #print(second)
        l=self.sortList(head)
        r=self.sortList(second)
        #print("l->",l)
        #print("r->",r)
        return self.mergeSort(l,r)
    
    def mergeSort(self,l,r):
        if l is None:
            return r
        elif r is None:
            return l
        dummy=ListNode(0)
        temp=dummy
        
        while l and r:
            if l.val<=r.val:
                temp.next=l
                l=l.next
            else:
                temp.next=r
                r=r.next
            temp=temp.next
        
        if r is None:
            temp.next=l
        else:
            temp.next=r
