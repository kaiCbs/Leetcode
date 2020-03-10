class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: 
        lists = [l for l in lists if l]
        if not lists:
            return None

        def mergeTwoLists(l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2
        i = 0
        while len(lists)>1:
            lists[i:i+2] = [mergeTwoLists(lists[i],lists[i+1])]
            i+=1
            if i == len(lists)-1 or i == len(lists):
                i = 0
        return lists[0]

# not good