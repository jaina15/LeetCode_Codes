# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.length(head)
        if not head or k==0 or not head.next or k==l:
            return head
        steps = l-(k%l)
        if steps == l:
            return head
        li,prev = head,None
        while li and steps>0:
            prev = li
            li = li.next
            steps-=1
        prev.next = None
        ans = li
        while li.next:
            li = li.next
        li.next = head
        return ans
    
    def length(self, head):
        l=0
        while head:
            head = head.next
            l+=1
        return l
