# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        headl1=list1
        temp1=list1
        temp2=list2
        headl2=list2
        tempb=list1
        
        #logic ko or optmize kar sakta tha, itti sari list lene k koi zarurat nhi thi
        for i in range(b):
            tempb=tempb.next
        #print(tempb)
        while temp2 and temp2.next:
            temp2=temp2.next
            
        temp2.next=tempb.next
        #print(temp2)
        #print(headl2)
        for i in range(a-1):
            temp1=temp1.next
        
        temp1.next=headl2
        #print(headl1)
        return headl1
