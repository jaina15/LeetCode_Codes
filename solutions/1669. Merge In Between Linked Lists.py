# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr,head=list1,list1
        l=b-a+1
        print(l)
        prev=None
        while curr and a>0:
            prev = curr
            curr = curr.next
            a-=1
        prev.next = list2
        
        while curr and l>0:
            curr = curr.next
            l-=1
        
        ans = head
        
        while head.next:
            head = head.next
        head.next = curr
        return ans
