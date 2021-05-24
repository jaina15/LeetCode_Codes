# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=n=ListNode()
        
        while(l1!=None and l2!=None):
            if(l1.val<=l2.val):
                n.next=ListNode(l1.val)
                n=n.next
                l1=l1.next
            else:
                n.next=ListNode(l2.val)
                n=n.next
                l2=l2.next
        if l1==None and l2!=None:
            n.next=l2
        elif l1!=None and l2==None:
            n.next=l1
        
       # print(ans.next)
        return ans.next
