class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        else:
            l1, l2 = head.next, head
        while 1:
            try:
                l1 = l1.next
                l2 = l2.next
                l1 = l1.next
                l1.next
            except AttributeError:
                return l2
            