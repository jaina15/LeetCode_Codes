# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        c=0
        flag=0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag=1
                c=self.lengthCycle(slow)
                break
        if not flag:
            return
        h1,h2=head,head
        while c>0:
            h1=h1.next
            c-=1
        
        while h1!=h2:
            h1=h1.next
            h2=h2.next
        return h1
    
    def lengthCycle(self,slow):
        temp = slow.next
        c=1
        while temp!=slow:
            temp = temp.next
            c+=1
