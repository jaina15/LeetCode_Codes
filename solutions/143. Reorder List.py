# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow.next
        
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        slow.next=None
        
        
        #ye tagda logic h, bahot tagda. Samjhana padega ise acche se
        #ye 2 list ko alternatively merge karne k liye h
        head1, head2 = head, prev
        
        while head2:
            next=head1.next
            head1.next=head2
            #print(head1)
            #print(head2)
            head1=head2
            head2=next
            #print(head1)
            #print(head2)
        
