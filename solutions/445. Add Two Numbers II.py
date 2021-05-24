# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #yes, i can solve it without reversing the input list
        num1=0
        while l1:
            num1=num1*10 + (l1.val)
            l1=l1.next
        
        num2=0
        while l2:
            num2=num2*10 + (l2.val)
            l2=l2.next
        
        res=num1+num2
        #print(res)
        ans=n=ListNode()
        #to return 0 list if sum is 0
        if res==0:
            return ans
        while(res):
            j=res%10
            n.next=ListNode(j)
            n=n.next
            res=res//10
        #to reverse output
        curr=ans.next
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        ans=prev
        return ans
