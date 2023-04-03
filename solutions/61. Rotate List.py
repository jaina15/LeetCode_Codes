# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last, n= head, 1
        if not head:
            return 
        while last.next:
            last = last.next
            n+=1
        k=k%n
        
        if k==0:
            return head
        
        last.next = head
        
        temp = head
        for _ in range(n-k-1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
