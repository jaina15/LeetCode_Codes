# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
            
        for i in range(0,len(l)-1,2):
        #    print(i)
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
        
        #print(l)
        
        head=dummy=ListNode(0)
        for i in l:
            dummy.next=ListNode(i)
            dummy=dummy.next
        
        return head.next
