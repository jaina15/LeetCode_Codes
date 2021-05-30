# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        ans.next=head
        prev=ans
        curr=head
        #full dekha h, khud nhi kar paya
        while curr and curr.next:
            if curr.val==curr.next.val:
                while curr.next and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else:
                prev=prev.next
                print(prev)
            curr=curr.next
        
        return ans.next
