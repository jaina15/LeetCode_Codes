# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k<=1 or head is None or head.next is None:
            return head
        
        temp=head
        l=0
        while temp:
            temp=temp.next
            l+=1
        #itti baar reverse karenge
        times=l//k
        temp=head
        dummy=ListNode(0)
        ans=dummy
        prev=head
        while times>0:
            n=k
            newhead=prev
            temp=prev
            #k nodes k list banane k liye
            while n>1 and temp:
                temp=temp.next
                n-=1
            prev=temp.next
            temp.next=None
            #print(temp)
            #print(prev)
            #print(newhead)
            curr=newhead
            pr=None
            while curr:
                next=curr.next
                curr.next=pr
                pr=curr
                curr=next
            newhead=pr
            #print(newhead)
            while dummy.next:
                dummy=dummy.next
            dummy.next=newhead
            #print(ans.next)
            times-=1
        #print(prev)
        #ye jab hume left out nodes ko bina reverse kie add karna h
        if prev:
            while dummy.next:
                dummy=dummy.next
            dummy.next=prev
        return ans.next
