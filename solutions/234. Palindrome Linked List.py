# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        init,slow,fast=head,head,head
        if head.next is None:
            return head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        curr=slow
        pre=None
        while slow:
            curr=slow
            slow=slow.next
            curr.next=pre
            pre=curr
        second=pre
        while init:
            if init.val!=second.val:
                return False
            init=init.next
            second=second.next
        return True
