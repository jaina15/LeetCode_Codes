        
        if l1:
            while l1:
                val = l1.val + carry
                if val>=10:
                    carry = 1
                    val%=10
                else:
                    carry = 0
                ans.next = ListNode(val)
                ans = ans.next
                l1 = l1.next
        if l2:
            while l2:
                val = l2.val + carry
                if val>=10:
                    carry = 1
                    val%=10
                else:
                    carry = 0
                ans.next = ListNode(val)
                ans = ans.next
                l2 = l2.next
        
        if carry:
            ans.next = ListNode(carry)
        return head.next
    
    
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         list1 = self.reverse(l1)
#         list2 = self.reverse(l2)
        
#         summ = self.number_from_list(list1) + self.number_from_list(list2)
#         return ListNode(0) if summ==0 else self.list_from_number(summ)
    
#     def reverse(self, head):
#         curr,prev = head,None
#         while curr:
#             nextt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextt
#         return prev
    
#     def number_from_list(self, head):
#         num = 0
#         while head:
#             num = num*10 + head.val
#             head = head.next
#         return num
    
#     def list_from_number(self, summ):
#         l = ListNode(-1)
#         head = l
#         while summ>0:
#             l.next = ListNode(summ%10)
#             l = l.next
#             summ//=10
#         return head.next
