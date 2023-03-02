# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        
        while curr:
            pres=curr
            while pres.next and pres.val==pres.next.val:
                pres=pres.next
            curr.next=pres.next
            curr=curr.next
        return head
