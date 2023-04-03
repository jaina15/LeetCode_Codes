# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        else:
            mid = self.getMiddle(head)
            prev = self.reverse(mid)
            head1, head2=head,prev
            while head2:
                nextt = head1.next
                head1.next = head2
                head1 = head2
                head2 = nextt
​
    def reverse(self,head):
        prev, curr = None, head
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
​
    def getMiddle(self,head):
        slow,fast = head,head
        prev=None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
