# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow=head,head
        length,flag=0,0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag=1
                length = self.length_of_cycle(slow)
                break
        
        if not flag:
            return
        
        first,second=head,head
        while length>0:
            first = first.next
            length-=1
        
        while first!=second:
            first = first.next
            second = second.next
        return second
            
    
    def length_of_cycle(self, head):
        temp = head.next
        l=1
        while temp != head:
            temp = temp.next
            l+=1
        return l
