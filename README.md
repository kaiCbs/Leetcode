


# Table of Contents
<!-- TOC -->

- [Table of Contents](#table-of-contents)
- [Data structure](#data-structure)
  - [Linkedlist](#linkedlist)
    - [2. Add Two Numbers](#2-add-two-numbers)
  - [Binary tree](#binary-tree)
    - [938. Range Sum of BST](#938-range-sum-of-bst)
  - [Stack](#stack)
    - [1021. Remove Outermost Parentheses](#1021-remove-outermost-parentheses)
- [Topics](#topics)
  - [Dynamic programming](#dynamic-programming)
    - [5. Longest Palindromic Substring](#5-longest-palindromic-substring)
    - [120. Triangle](#120-triangle)
    - [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
  - [Two pointers](#two-pointers)
    - [3. Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters)
    - [15. 3Sum](#15-3sum)
    - [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)
    - [27. Remove Element](#27-remove-element)
  - [Binary Search](#binary-search)
    - [278. First Bad Version](#278-first-bad-version)
    - [852. Peak Index in a Mountain Array](#852-peak-index-in-a-mountain-array)
  - [Greedy](#greedy)
    - [55. Jump Game](#55-jump-game)
  - [Bit Manipulation](#bit-manipulation)
    - [136. Single Number](#136-single-number)
- [Note](#note)
  - [Trees](#trees)
    - [Binary Search Tree](#binary-search-tree)
    - [Traverse a Tree](#traverse-a-tree)

<!-- /TOC -->







# Data structure
## Linkedlist
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
## Binary tree
### [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

```
def
```
Use property of [BST](#binary-search-tree) to save time, (no need to traverse all sub-trees).

## Stack 

### [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)

```
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        ans = ''
        for i in S:
            if not stack:
                stack.append(i) 
            elif (stack == ['(']) and (i==')'):
                stack.pop()
            else:
                if i==')':
                    stack.pop()
                if i=='(':
                    stack.append(i)
                ans += i
        return ans
```








# Topics
## Dynamic programming

### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)


### [120. Triangle](https://leetcode.com/problems/triangle/)
```
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        last = []
        for row in triangle:
            if last:
                row[0] += last[0]
                row[-1] += last[-1]
            for i in range(len(last)-1):
                row[i+1] = min(row[i+1]+last[i],row[i+1]+last[i+1])
            last = row
        return min(last)
```
Time complexity o(n^2)

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice = prices[0]
        profit = 0
        for p in prices[1:]:
            profit = max(profit, p-minPrice)
            minPrice = min(minPrice,p)
        return profit
```
record **minimum price in history** and **maximum profit** and update.


## Two pointers

### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        ans, i, j, searchDict = 1, 0, 0, {}
        searchDict[s[0]] = 0
        while j<len(s)-1:
            j+=1
            if s[j] in searchDict:
                if (searchDict[s[j]]<i):
                    searchDict[s[j]] = j
                else:
                    i = searchDict[s[j]]+1
                    searchDict[s[j]] = j
            else:
                searchDict[s[j]] = j
            ans = max(ans,j-i+1)
        return ans
```
Use two pointers to construct a slicing window. Expand the window to get the longest substring without repeating characters. View article [here](https://leetcode.com/articles/longest-substring-without-repeating-characters/).


### [15. 3Sum](https://leetcode.com/problems/3sum/)

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, result = len(nums), set()
        nums.sort()
        for i in range(n-2):
            l, r = i+1, n-1
            while l<r:
                sum3 = nums[i]+nums[l]+nums[r]
                if sum3 == 0:
                    result.add((nums[i],nums[l],nums[r]))
                    r-=1
                elif sum3 > 0:
                    r-=1
                else:
                    l+=1
        return result
```
Time complexity O(n^2)


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
The tricky point is we need to remove the duplicates **in-place**, thus we need two pointers, one iterate the list, the other records unique number's index. 


### [27. Remove Element](https://leetcode.com/problems/remove-element/description/)
```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0;
        for i in nums:
            if i!=val:
                nums[idx] = i
                idx+=1
        return idx
```
Similar with [problem 26](#26-remove-duplicates-from-sorted-array). Just iterate the list, drag valid number to the head.

## Binary Search

### [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)
```
class Solution:
    def firstBadVersion(self, n, m=0):
        """
        :type n: int
        :rtype: int
        """
        if n==m+1:
            return n
        mid = (m+n)//2
        if isBadVersion(mid):
            return Solution.firstBadVersion(self,mid,m)
        else:
            return Solution.firstBadVersion(self,n,mid)
```

### [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

```
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        w = len(A)
        if w == 3:
            return 1
        left, right = 0, w-1
        mid = (left + right)//2
        if A[mid-1] < A[mid] > A[mid+1]:
            return mid
        if A[mid] > A[mid+1]:
            return self.peakIndexInMountainArray(A[:mid+1])
        else:
            return mid + self.peakIndexInMountainArray(A[mid:])
```

## Greedy
### [55. Jump Game](https://leetcode.com/problems/jump-game/)

```
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return true
        des = len(nums)-1
        nowMax = nums[0]
        nowId = 0
        while (nowMax<des) & (nowId < nowMax):
            nowId += 1
            if nowMax < nowId + nums[nowId]:
                nowMax = nowId + nums[nowId]
        return (nowMax>=des)           
```

## Bit Manipulation
### [136. Single Number](https://leetcode.com/problems/single-number/)

```
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r^=i
        return r
```
use "^" (Caret), XOR operator













# Note

## Trees

### Binary Search Tree

> Binary Search Tree is a node-based binary tree data structure which has the following properties:
> - The left subtree of a node contains only nodes with keys lesser than the node’s key.
> - The right subtree of a node contains only nodes with keys greater than the node’s key.
> - The left and right subtree each must also be a binary search tree.


### Traverse a Tree
> - **Pre-order** traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree. 
> - **In-order** traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
> - **Post-order** traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.