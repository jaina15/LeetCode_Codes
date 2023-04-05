# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,count,k=head,0,2
        while curr and count<k:
            curr=curr.next
            count+=1
        if count<k:
            return head
        new_head,prev = self.reverse(head,k)
        head.next = self.swapPairs(new_head)
        return prev
    
    def reverse(self, head, count):
        curr,prev=head,None
        while curr and count>0:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
            count-=1
        return (curr,prev)
