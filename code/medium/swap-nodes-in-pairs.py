class Solution(object):
    def swapPairs(self, head):
        if (head == None) or (head.next == None):
            return head
        subHead = head.next.next
        newHead = head.next
        newHead.next = head
        head.next = self.swapPairs(subHead)
        return newHead
        
        