# Table of Contents 

Date: 2019-10-29
Progress: [101/1212]

<!-- TOC -->

- [Table of Contents](#table-of-contents)
- [Data structure](#data-structure)
  - [String](#string)
    - [6. ZigZag Conversion](#6-zigzag-conversion)
    - [8. String to Integer (atoi)](#8-string-to-integer-atoi)
  - [Array](#array)
    - [48. Rotate Image](#48-rotate-image)
  - [Linkedlist](#linkedlist)
    - [2. Add Two Numbers](#2-add-two-numbers)
    - [21. Merge Two Sorted Lists](#21-merge-two-sorted-lists)
    - [24. Swap Nodes in Pairs](#24-swap-nodes-in-pairs)
    - [86. Partition List](#86-partition-list)
    - [237. Delete Node in a Linked List](#237-delete-node-in-a-linked-list)
  - [Stack and Queue](#stack-and-queue)
    - [20. Valid Parentheses](#20-valid-parentheses)
    - [921. Minimum Add to Make Parentheses Valid](#921-minimum-add-to-make-parentheses-valid)
    - [1021. Remove Outermost Parentheses](#1021-remove-outermost-parentheses)
  - [Tree and Graph](#tree-and-graph)
    - [98. Validate Binary Search Tree](#98-validate-binary-search-tree)
    - [938. Range Sum of BST](#938-range-sum-of-bst)
  - [Heap](#heap)
  - [Hash Table](#hash-table)
    - [1. Two Sum](#1-two-sum)
    - [49. Group Anagrams](#49-group-anagrams)
- [Algorithm](#algorithm)
  - [Sorting](#sorting)
    - [56. Merge Intervals](#56-merge-intervals)
    - [75. Sort Colors](#75-sort-colors)
    - [179. Largest Number](#179-largest-number)
  - [Searching](#searching)
  - [Dynamic programming](#dynamic-programming)
    - [5. Longest Palindromic Substring](#5-longest-palindromic-substring)
    - [39. Combination Sum](#39-combination-sum)
    - [53. Maximum Subarray](#53-maximum-subarray)
    - [120. Triangle](#120-triangle)
    - [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
    - [198. House Robber](#198-house-robber)
    - [303. Range Sum Query - Immutable](#303-range-sum-query---immutable)
    - [338. Counting Bits](#338-counting-bits)
    - [746. Min Cost Climbing Stairs](#746-min-cost-climbing-stairs)
  - [Graph Theory](#graph-theory)
- [Topics](#topics)
  - [Two pointers](#two-pointers)
    - [3. Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters)
    - [11. Container With Most Water](#11-container-with-most-water)
    - [15. 3Sum](#15-3sum)
    - [19. Remove Nth Node From End of List](#19-remove-nth-node-from-end-of-list)
    - [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)
    - [27. Remove Element](#27-remove-element)
    - [42. Trapping Rain Water](#42-trapping-rain-water)
  - [Binary Search](#binary-search)
    - [4. Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays)
    - [50. Pow(x, n)](#50-powx-n)
    - [278. First Bad Version](#278-first-bad-version)
    - [852. Peak Index in a Mountain Array](#852-peak-index-in-a-mountain-array)
  - [Greedy](#greedy)
    - [55. Jump Game](#55-jump-game)
    - [134. Gas Station](#134-gas-station)
  - [Bit Manipulation](#bit-manipulation)
    - [136. Single Number](#136-single-number)
  - [Backtracking](#backtracking)
    - [22. Generate Parentheses](#22-generate-parentheses)
- [Note](#note)
  - [Trees](#trees)
    - [Binary Search Tree](#binary-search-tree)
    - [Traverse a Tree](#traverse-a-tree)
  - [Sorting Algorithms](#sorting-algorithms)
    - [Bubble Sort](#bubble-sort)
    - [Quick Sort](#quick-sort)
    - [Merge Sort](#merge-sort)
  - [Wheels](#wheels)
    - [prime generator](#prime-generator)

<!-- /TOC -->

# Data structure

## String
### [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: return s
        Key = sorted([(-abs((i%((numRows-1)*2))+1-numRows),i) for i in range(len(s))])
        return ''.join([s[i[1]] for i in Key])
```
Mod(2*row-1), same pattern

### [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
```
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        rex = re.match(' *([-+]?\d+)',str)
        if rex:
            value = int(rex.group(1))
            return max(min(value,2**31-1),-2**31)
        else:
            return 0
```
See how regular expression simplifies life.

## Array
### [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[r[i]for r in matrix[::-1]] for i in range(len(matrix))] 
```


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

### [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

```
class Solution(object):
    def mergeTwoLists(self, l1, l2):
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
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

[@greatgrahambini](https://leetcode.com/greatgrahambini/): While this is indeed elegant, it should be noted that this would be a terrible solution from a practical point of view, as the stack size would be equal to the length of the merged list, which would result in a stack overflow for relatively small lengths of lists

### [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

```
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        subHead = head.next.next
        newHead = head.next
        newHead.next = head
        head.next = self.swapPairs(subHead)
        return newHead
```
Recursion is trivial, however, we need to know how to do it in an iterative way. Here we go
```
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next
```

### [86. Partition List](https://leetcode.com/problems/partition-list/)
```
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
```
Dummy heads, one pass.

### [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

```
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

[@barrywuh](https://leetcode.com/barrywuh/): I was kind of doubting the correctness of the problem since I thought without giving a head, I cannot delete the node. Then I found that some guys are smart. They change value. :D!  
[@songjiang951130](https://leetcode.com/songjiang951130/): Copy the value of next value and delete next node.

## Stack and Queue

### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
```
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if stk and stk[-1]+i in ['{}','[]','()']:
                stk.pop()
            else:
                stk.append(i)
        return not stk
```

### [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

```
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = []
        for i in S:
            if not ans:
                ans.append(i)
            elif ans[-1] + i == '()':
                ans.pop()
            else:
                ans.append(i)
        return len(ans)
```

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

## Tree and Graph

### [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
```
class Solution:
    def isValidBST(self, root: TreeNode, mi = float('-inf'), ma = float('inf')) -> bool:
        if not root:
            return True
        if (root.val >= ma) or (root.val <= mi):
            return False
        return self.isValidBST(root.left,mi,root.val) and self.isValidBST(root.right,root.val,ma)
```

### [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

```
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root: return 0
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        if root.val > R : return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```
Use property of [BST](#binary-search-tree) to save time, (no need to traverse all sub-trees).

## Heap


## Hash Table
### [1. Two Sum](https://leetcode.com/problems/two-sum/)

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            if num in h:
                return [i,h[num]]
            h[target-num] = i
```
Use hash table to reduce time complexity. O(n), push number meanwhile check for pairs.

### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            ans.setdefault("".join(sorted(i)),[]).append(i)
        return ans.values()
```
Use Hash table, and notice the usage of *.setdefault*

# Algorithm

## [Sorting](#sorting-algorithms)

### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
```
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for itv in intervals[1:]:
            if itv[0]<=ans[-1][1]:
                ans[-1][1] = max(itv[1],ans[-1][1])
            else:
                ans.append(itv)
        return ans
```
Sort the intervals by their start value, then merge them one by one.

### [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
```
void sortColors(int A[], int n) {
    int n0 = -1, n1 = -1, n2 = -1;
    for (int i = 0; i < n; ++i) {
        if (A[i] == 0) 
        {
            A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
        }
        else if (A[i] == 1) 
        {
            A[++n2] = 2; A[++n1] = 1;
        }
        else if (A[i] == 2) 
        {
            A[++n2] = 2;
        }
    }
}
```
The Dutch National Flag Problem. Great Video [here](https://www.youtube.com/watch?v=ER4ivZosqCg).

### [179. Largest Number](https://leetcode.com/problems/largest-number/)

```
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str,nums),key = lambda x: x+x, reverse = True))
```
cmp in Python2 now are functools.cmp_to_key

## Searching 

## Dynamic programming

### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''      
        s = '*'+s
        dic = {(1,2):1}
        ans = s[1]
        i,j = 1,2
        hisLong, lastLongStart = (1,2), 1
        while j < len(s):
            dic[(j,j)], dic[(j,j+1)],dic[(j+1,j)] = 1, 1, 1
            cur = lastLongStart
            while not (dic[(cur,j)] and (s[cur-1] == s[j])):
                dic[(cur-1,j+1)] = 0
                cur+=1
            lastLongStart = max(cur,lastLongStart)-1
            dic[(lastLongStart,j+1)] = 1
            if (j+1-lastLongStart) > (hisLong[1]-hisLong[0]):
                hisLong = (lastLongStart,j+1)
            for m in range(cur+1,j+2):
                if (dic[(m,j)] and (s[m-1] == s[j])):
                    dic[(m-1,j+1)] = 1
                else:
                    dic[(m-1,j+1)] = 0
            j+=1
        return s[hisLong[0]:hisLong[1]]
```
### [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 0:
            return []
        elif target == 0:
            return [[]]
        if candidates==[]:
            return []
        return [[candidates[0]]+i for i in self.combinationSum(candidates,target-candidates[0])] + self.combinationSum(candidates[1:],target)
```

### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maxsub = [0,0,nums[0]]
        for n in nums:
            maxsub[0] = (max(maxsub[0],0) + n)
            maxsub[1] = max(maxsub[1],maxsub[0],n)
            maxsub[2] = max(maxsub[2],n)
        if maxsub[2] < 0:
            return maxsub[2]
        return max(maxsub)
```
Consider maximum sum with and without the last number.


```
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)
```
Cleverest solution from [@_LeetCode](https://leetcode.com/_leetcode/), Orz

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

### [198. House Robber](https://leetcode.com/problems/house-robber/)

```
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return sum(nums)
        money = [nums[0],nums[1]]
        for i in range(len(nums)-2):
            money = [max(money[0],money[1]), (money[0]+nums[i+2])]
        return max(money)
```
record and update the tuple (gain1,gain2), where gain1 is the gain that robber robbed the last house, gain2 is the gain he didn't.

### [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

```
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumsum = [0]
        temp = 0
        for i in nums:
            temp += i
            self.cumsum.append(temp)    

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumsum[j+1] - self.cumsum[i]  
```
Pre-compute the cumulative sum.

### [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

```
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(1,num+1):
            ans.append(ans[i//2] + i%2)
        return ans
```
Keep in mind: f(n) = f(n//2) + n%2

### [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

```
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 3:
            return min(cost)
        mincost = [cost[0],cost[1]]
        for i in range(len(cost)-2):
            mincost[0], mincost[1] = mincost[1], min(mincost)+cost[i+2]
        return min(mincost)
```

## Graph Theory

# Topics
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

### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        ans = (j-i) * min(height[i],height[j])
        while j-i>0:
            if height[i] < height[j]:
                water = height[i]*(j-i)
                i+=1
            else:
                water = height[j]*(j-i)
                j-=1
            if water > ans:
                ans = water
        return ans
```
Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. 

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

### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
```
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
```


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

### [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
```
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0 ,len(height)-1
        ans = 0
        while i<j-1:
            leftMark, rightMark = height[i], height[j]
            if height[i] <= height[j]:
                i+=1
                while height[i] < leftMark:
                    ans += (leftMark-height[i])
                    i+=1
            else:
                j-=1
                while height[j] < rightMark:
                    ans += (rightMark-height[j])
                    j-=1
        return ans
```

## Binary Search

### [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

```
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2,sp1=0,sp2=0,l1=0,l2=0):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if l1+l2==0:
            l1,l2 = len(nums1),len(nums2)
        def mid(num,sp,l):
            midValue = (num[sp+l//2]+num[sp+(l-1)//2])/2
            return midValue
        if (l1>l2+4):
            sp1 +=(l1-l2-1)//2
            l1 -= ((l1-l2-1)//2) * 2
        elif (l2>l1+4):
            sp2 += (l2-l1-1)//2
            l2 -= ((l2-l1-1)//2) * 2
        while (l1+l2)>10:
            lmin = min(l1,l2)
            st = (lmin+1)//2-1
            if mid(nums1, sp1, l1) < mid(nums2, sp2, l2):
                return self.findMedianSortedArrays(nums1, nums2,sp1=sp1+st,sp2=sp2,l1=l1-st,l2=l2-st)
            elif mid(nums1, sp1, l1) > mid(nums2, sp2, l2):
                return self.findMedianSortedArrays(nums1, nums2,sp1=sp1,sp2=sp2+st,l1=l1-st,l2=l2-st)
            else:
                return mid(nums1, sp1, l1)
        new = sorted(nums1[sp1:sp1+l1]+nums2[sp2:sp2+l2])
        return mid(new,0,l1+l2)
```


### [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
```
def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n==0:
        return 1
    if n<0:
        return self.myPow(1/x,-n)
    ans = 1
    while n>0:
        x_p,p = x,1
        while 2*p <= n:
            p*=2
            x_p = x_p * x_p
        ans *= x_p
        n -= p
    return ans
```
Fast Power. O(ln N)

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

### [134. Gas Station](https://leetcode.com/problems/gas-station/)
```
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N, allGas, lowest, ans = len(gas), 0, 0, 0
        for i in range(N):
            allGas += (gas[i]-cost[i])
            if allGas <= lowest:
                lowest = allGas
                ans = i
        if allGas<0:
            return -1
        return (ans+1)%N
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

## Backtracking

### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def GP(l, r, cum):
            if l == 0:
                return [')'*r]
            if cum == 0:
                return ['('+c for c in GP(l-1, r, cum+1)]
            else:
                return ['('+ c for c in GP(l-1, r, cum+1)] + [')'+ c for c in GP(l, r-1, cum-1)]  
        return GP(n,n,0
```










# Note

## Trees

### Binary Search Tree

 Binary Search Tree is a node-based binary tree data structure which has the following properties:
 - The left subtree of a node contains only nodes with keys lesser than the node’s key.
 - The right subtree of a node contains only nodes with keys greater than the node’s key.
 - The left and right subtree each must also be a binary search tree.


### Traverse a Tree
 - **Pre-order** traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree. 
 - **In-order** traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
 - **Post-order** traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.


## Sorting Algorithms
### Bubble Sort
```
def bubblesort(arr):                               
    n = len(arr)                                 
    for i in range(n-1):                          
        for j in range(n-i-1):                     
            if arr[j]>arr[j+1]:                    
                arr[j],arr[j+1] = arr[j+1],arr[j] 
```
### Quick Sort
```
def partition(arr,left,right):                     
    pivot = arr[right]    
    id = left          
    while left < right:      
        if arr[left] < pivot:   
            arr[left], arr[id] = arr[id], arr[left]
            id+=1                
        left += 1        
    arr[id], arr[right] = arr[right], arr[id]     
    return id                                                 
                                    
                             
def quicksort(lst):
    def sortBy(lst,left,right):         
        if left<right:                 
            mid = partition(lst,left,right)       
            sortBy(lst,left,mid-1)      
            sortBy(lst,mid+1,right)              
    sortBy(lst,0,len(lst)-1)                                 
```


### Merge Sort


## Wheels
### prime generator
```
def divide(n): 
    return lambda x: x % n > 0

def primes(k): 
        ans = [2] 
        n=2 
        it = iter(range(3,2*k,2))  
        while n<k: 
            n = next(it)  
            ans.append(n) 
            it = filter(divide(n), it) 
        ans.pop() 
        return ans 
``` 