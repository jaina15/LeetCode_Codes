# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans=n=head
        #print(n)
        while n:
            while n.next and n.val == n.next.val:
                n.next=n.next.next
            n=n.next
            #ans.next=n
            
        #print(head)
        return head
