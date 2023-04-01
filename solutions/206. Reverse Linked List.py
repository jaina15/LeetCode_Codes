# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    #this is recursive solution
    #    return self.helper(head,None)
    
    #def helper(self,curr,prev):
    #    if curr is None:
    #        return prev
    #    nxt = curr.next
    #    curr.next = prev
    #    return self.helper(nxt,curr)
