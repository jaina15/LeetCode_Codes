# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        k=0
        while temp:
            k+=1
            temp=temp.next
        if k==1 and n==1:
            return ListNode('')
        
        temp=head
        prev=None
        l=(k-n+1)
        i=1
        while(temp and i<l):
            prev=temp
            temp=temp.next
            i+=1
        if temp==head:
            head=head.next
        else:
            prev.next=temp.next
        #print(head)
        return head
