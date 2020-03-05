class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = ListNode(1)
        c_l1 = l1
        l2 = ListNode(1)
        c_l2 = l2   
        while head:
            if head.val < x:
                c_l1.next = head
                c_l1 = head
                c_l2.next = None
            else:
                c_l2.next = head
                c_l2 = head
                c_l1.next = None
            head = head.next
        c_l1.next = l2.next
        return l1.next