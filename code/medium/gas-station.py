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