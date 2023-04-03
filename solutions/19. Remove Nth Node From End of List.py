# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # this is naive solution    
    #    if not head:
    #        return
    #    curr,length = head,0
    #    while curr:
    #        curr,length=curr.next,length+1
    #    if n>length:
    #        return
    #    if n==length:
    #        return head.next
    #    c=length-n
    #    curr,prev=head,None
    #    while c>0:
    #        prev=curr
    #        curr=curr.next
    #        c-=1
    #    prev.next = curr.next
    #    return head
    
    # this is one pass solution
        slow,fast = head,head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
​
        while fast.next:
            fast,slow = fast.next,slow.next
        slow.next = slow.next.next
        return head
