# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        ans_head = ans
        curr = head.next
        val=0
        while curr:
            val += curr.val
            if curr.val==0:
                ans.next = ListNode(val)
                ans = ans.next
                val = 0
            curr = curr.next
        return ans_head.next
            
