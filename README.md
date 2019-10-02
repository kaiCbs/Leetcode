
# Table of Contents
<!-- TOC -->

- [Table of Contents](#table-of-contents)
- [Problems](#problems)
  - [Data structure](#data-structure)
    - [2. Add Two Numbers](#2-add-two-numbers)
  - [Dynamic programming](#dynamic-programming)
  - [Two pointers](#two-pointers)
    - [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)

<!-- /TOC -->
# Problems 
## Data structure
### [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)
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


## Two pointers
### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        L = len(nums)
        lastValue = nums[0]
        result = 0
        for i in range(1,L):
            if nums[i] != lastValue:
                lastValue = nums[i]
                result += 1
                nums[result] = lastValue
                
        return result+1
```
The tricky point is we need to remove the duplicates in-place, thus we need two pointers, one iterate the list, the other records unique number's index. 