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
