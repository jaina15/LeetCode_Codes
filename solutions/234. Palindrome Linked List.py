# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head
        prev,slow,fast = None,head,head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        pre,curr = None,slow
        while curr:
            nextt = curr.next
            curr.next = pre
            pre = curr
            curr = nextt
        
        first,second = head,pre
