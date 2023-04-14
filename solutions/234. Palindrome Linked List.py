# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head
        slow,fast = head,head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        curr,prev = slow,None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        while head:
            if head.val!=prev.val:
                return False
            head = head.next
            prev = prev.next
        
