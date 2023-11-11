# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.reverse(head)
        ans = ListNode(-1)
        head = ans
        numm,c=0,0
        while l:
            val = 2*(l.val)
            act_val=0
            if c>0:
                act_val = val%10 + c
                c-=1
            else:
                act_val = val%10
            c = val//10
            ans.next = ListNode(act_val)
            ans = ans.next
            l = l.next
        if c>=1:
            ans.next = ListNode(c)
            ans = ans.next
        return self.reverse(head.next)
    
    def reverse(self, head):
        curr,prev = head,None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
