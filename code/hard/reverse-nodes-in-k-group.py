class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        newHead = None
        marker = head
        for i in range(k): 
            if head == None:
                return self.reverseKGroup(newHead,i)
            temp = head.next
            head.next = newHead
            newHead = head
            head = temp
            
        marker.next = self.reverseKGroup(head,k)
        return newHead
        
