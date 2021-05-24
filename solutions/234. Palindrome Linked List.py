# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s=''
        while(head):
            s+=str(head.val)
            head=head.next
      # print(s)
      # print(s[::-1])
        if s==s[::-1]:
            return True
        else:
            return False
