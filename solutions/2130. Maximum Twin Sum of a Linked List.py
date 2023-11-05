# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast,prev = head,head,None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        curr = slow
        pre = None
        while curr:
            nextt = curr.next
            curr.next = pre
            pre = curr
            curr= nextt
        
        second = pre
        first = head
        
        maxi=0
        while first:
            maxi = max(maxi,first.val+second.val)
            first = first.next
            second = second.next
        return maxi
