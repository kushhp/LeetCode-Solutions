# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        l3 = dummy
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
                l1 = None
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
                l2 = None
            val = (val1+val2+carry)%10
            carry = (val1+val2+carry)//10
            l3.next = ListNode(val)
            l3 = l3.next
        return dummy.next