# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        odd=head
        even=head.next
        evens=even
        
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            
            odd=odd.next
            even=even.next
        
        odd.next=evens
        return head
