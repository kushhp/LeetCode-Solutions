class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return
        dummy = ListNode(-1)
        dummy.next = head
        i=0
        while head.next:
            i+=1
            if(i%2!=0):
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
            head = head.next
        return dummy.next