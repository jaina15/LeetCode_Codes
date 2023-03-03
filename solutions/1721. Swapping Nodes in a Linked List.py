# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l[k-1],l[len(l)-k]=l[len(l)-k],l[k-1]
        head=ans=ListNode(0)
        for i in l:
            ans.next=ListNode(i)
            ans=ans.next
        return head.next
