
# Table of Contents
<!-- TOC -->

- [Table of Contents](#table-of-contents)
- [Problems](#problems)
  - [Data structure](#data-structure)
    - [2. Add Two Numbers](#2-add-two-numbers)
  - [Dynamic programming](#dynamic-programming)

<!-- /TOC -->
# Problems 
## Data structure
### 2. Add Two Numbers
```
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:

        c,v = (l1.val+l2.val+c)//10,(l1.val+l2.val+c)%10
        result = ListNode(v) 
        if ((l1.next!=None) or (l2.next!=None) or (c!=0)):
            if l1.next==None:
                l1.next = ListNode(0)
            if l2.next==None:
                l2.next = ListNode(0)                
            nextValue = Solution.addTwoNumbers(self,l1.next,l2.next,c)
        else:
            nextValue = None
        result.next = nextValue
        return result
```     

## Dynamic programming