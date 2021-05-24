# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr=l1
        prev=None
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        l1=prev
        num1=0
        while(l1):
        #    print(l1.val,end="->")
            num1=num1*10+(l1.val)
            l1=l1.next
        
        curr=l2
        prev=None
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        l2=prev
        num2=0
        while(l2):
        #    print(l1.val,end="->")
            num2=num2*10+(l2.val)
            l2=l2.next
            
        #print(num1)
        #print(num2)
        res=num1+num2
        #print(res)
        ans=n=ListNode()
        if res==0:
            return ans
        #print(ans)
        while(res):
            j=res%10
            n.next=ListNode(j)
            n=n.next
            res=res//10
        
        #print(ans.next)
        return ans.next
            
