class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        rev = None
        while temp:
            a = temp.next
            temp.next = rev
            rev = temp
            temp = a
        return rev
            