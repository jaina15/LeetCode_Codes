# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        init,slow,fast=head,head,head
        last,prev=None,None
        
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None
        #print(init)
        #print(second)
        
        pre=None
        while second:
            curr=second
            second=second.next
            curr.next=pre
            pre=curr
        #print(pre)
        
        ans=-1
        while init:
            ans=max(ans,init.val+pre.val)
            init=init.next
            pre=pre.next
        return ans
#6
#0   6-1-0   5
#1   6-1-1   4
#2   6-1-2   3
#3   6-1-3   2
#4   6-1-4   1
#5   6-1-5   0
​
#6   8   5   1   2   4
​
​
