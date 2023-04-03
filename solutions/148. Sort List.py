# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.getMiddle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.mergeTwoLists(left,right)
    
    def getMiddle(self, head):
        slow, fast = head, head
        prev=None
        while fast and fast.next:
            prev=slow
            slow =slow .next
            fast = fast.next.next
        prev.next=None
        return slow
        
    def mergeTwoLists(self, list1, list2):
        curr = ans = ListNode()
        
        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return ans.next
