class Solution(object):
    def getIntersectionNode(self, headA, headB):
        bhead = headB
        ahead = headA
        if not (headB and headA):
            return None
        while headB.next != headA.next:
            if headA.next == None:
                headA = bhead
            else: 
                headA = headA.next
            if headB.next == None:
                headB = ahead
            else:
                headB = headB.next
        if headB == headA:
            return headB
        elif headB.next:
            return headB.next
        return None

# not good