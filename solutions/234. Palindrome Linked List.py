# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev,slow,fast=None,head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
