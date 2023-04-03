# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head or m==n or head.next is None:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr = dummyNode
        prev=None
        for i in range(m-1):
            prev=curr
            curr=curr.next
        
        new_curr=curr.next
        curr.next=None
        point = new_curr
        prev=None
        for i in range(n-m+1):
            nxt=new_curr
            new_curr=new_curr.next
            nxt.next=prev
            prev=nxt
        curr.next=prev
        point.next=new_curr
        return dummyNode.next
