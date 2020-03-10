class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def count1(num):
            count = 0
            while num:
                num &= (num-1)
                count+=1
            return count
        return ["%d:%02d"%(i,j) for i in range(12) 
                for j in range(60) if count1(i)+count1(j)==num]
