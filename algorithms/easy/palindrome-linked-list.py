class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow, flag = head, head, 0
        while fast:
            fast = fast.next
            if flag:
                slow = slow.next
            flag = 1-flag
            
        def reverseList(head: ListNode) -> ListNode:
            temp = head
            rev = None
            while temp:
                a = temp.next
                temp.next = rev
                rev = temp
                temp = a
            return rev
    
        rev = reverseList(slow)

        while head and rev:
            if rev.val!=head.val:
                return False
            rev,head = rev.next,head.next
        return True

# not good