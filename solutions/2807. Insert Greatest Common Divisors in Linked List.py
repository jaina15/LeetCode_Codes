# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head.next
        while fast:
            val = gcd(slow.val,fast.val)
            nxt = slow.next
            slow.next = ListNode(val)
            slow.next.next = fast
            slow = fast
            fast = fast.next
        
        return head
    
    @staticmethod
    def gcd(a,b):
        if (b == 0):
             return a
        return gcd(b, a%b)
