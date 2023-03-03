# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modi,curr=ListNode(0),head
        modi.next=head
        while curr.next:
            if curr.val==0:
                modi.next=curr
                modi=modi.next
            modi.val+=curr.val
            curr=curr.next
        modi.next=None
        return head
