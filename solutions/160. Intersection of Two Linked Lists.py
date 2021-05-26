# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s=set()
        tempa=headA
        tempb=headB
        la=0
        lb=0
        while(tempa):
            la+=1
            tempa=tempa.next
        
        while(tempb):
            lb+=1
            tempb=tempb.next
        
        if(la<=lb):
            tempa=headA
            tempb=headB
            while(tempa):
                s.add(tempa)
                tempa=tempa.next
            
            while(tempb):
                if(tempb in s):
                    return tempb
                tempb=tempb.next
​
        else:
            tempa=headA
            tempb=headB
            while(tempb):
                s.add(tempb)
                tempb=tempb.next
            
            while(tempa):
                if(tempa in s):
                    return tempa
                tempa=tempa.next
                
        return None
