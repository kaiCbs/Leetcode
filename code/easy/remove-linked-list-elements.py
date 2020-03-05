class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head:
            if head.val == val:
                return self.removeElements(head.next,val)
            else:
                head.next = self.removeElements(head.next,val)
                return head
        else:
            return None