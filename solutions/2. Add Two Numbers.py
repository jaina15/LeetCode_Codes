# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(-1)
        head = ans
        carry = 0
        
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val>=10:
                carry = 1
                val%=10
            else:
                carry = 0
            ans.next = ListNode(val)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                val = l1.val + carry
                if val>=10:
                    carry = 1
                    val%=10
                else:
                    carry = 0
                ans.next = ListNode(val)
                ans = ans.next
                l1 = l1.next
        if l2:
            while l2:
                val = l2.val + carry
                if val>=10:
                    carry = 1
                    val%=10
                else:
                    carry = 0
                ans.next = ListNode(val)
                ans = ans.next
                l2 = l2.next
        
        if carry:
            ans.next = ListNode(carry)
        return head.next
    
    
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
