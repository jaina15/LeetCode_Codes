# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l=[]
        if root is None:
            while k>0:
                l.append(ListNode(''))
                k-=1
            return l
        elif k==0:
            return l
        
        temp=root
        c=0
        while temp:
            temp=temp.next
            c+=1
        if c<k:
            temp=root
            while temp:
                l.append(ListNode(temp.val))
                temp=temp.next
                
            while len(l)<k:
                l.append(ListNode(''))
        else:
            m=c%k
            lp=k
            prevnext=root
            while lp>0:
                d=int(c/k)
                #print(d)
                node=prevnext
                #print(node)
                hd=node
                while node and d>1:
                    node=node.next
                    d-=1
                if m>0:
                    node=node.next
                    m-=1
                prevnext=node.next
                #print(prevnext)
                node.next=None
                #print(hd)
                l.append(hd)
                lp-=1
        return l
