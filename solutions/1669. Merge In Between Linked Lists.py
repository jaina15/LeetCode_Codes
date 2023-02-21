# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev,check_a,check_b=None,None,None
        init,head=list1,list1
        c=0
        while list1:
            if a==c:
                check_a=prev
            if b==c:
                check_b=list1.next
            c+=1
            prev=list1
            list1=list1.next
        #print(check_a,check_b)
        check_a.next=list2
        while init.next:
            init=init.next
        init.next=check_b
        return head
