# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        prev=None
        revs=None
        revsprev=None
        revend=None
        revendnext=None
        curr=head
        initial=head
        #starting position
        p=1
        f=0
        if(p==1 and left==1):
            f=1
        while(curr and p<left):
            revsprev=curr
            curr=curr.next
            p+=1
        revs=curr
        while(curr and p<right):
            curr=curr.next
            p+=1
        revend=curr
        revendnext=curr.next
        revend.next=None
      # print(revs.val)
       #print(revsprev.val)
      # print(revend.val)
      # print(revendnext.val)
        
        #curr=revs
        #while(curr is not None):
        #   print(curr.val,end='->')
        #    curr=curr.next
        #urr=revs
        while(revs is not None):
            next=revs.next
            revs.next=prev
            prev=revs
            revs=next
        revs=prev
        #rint(revs)
        if f==0:
            revsprev.next=revs
            revs=revsprev
        else:
            head=revs
        
        while(revs.next is not None):
            revs=revs.next
        revs.next=revendnext
#       head=prev
 #      print(head)
 #      if f==0:
 #          revsprev.next=head
 #          head=revsprev
#       curr=head
#   #   print(head)
#       while(curr.next is not None):
#       #    print(curr.val,end='->')
#           curr=curr.next
 #      curr.next=revendnext
        return head
        
        
