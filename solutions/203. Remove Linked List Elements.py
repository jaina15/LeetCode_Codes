# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        
        temp = head
        prev=None
        while temp:
            if temp.val==val:
                # ye wala if jo head element ka h mujhe baar baar isme problem hoti h. ise dhyan me rakhna h
                if temp==head:
                    temp=head.next
                    head=head.next
                else:
                    prev.next=temp.next
                    temp=temp.next
            else:
                prev=temp
                temp=temp.next
            
        return head
