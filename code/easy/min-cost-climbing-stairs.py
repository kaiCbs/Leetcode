class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost) < 3:
            return min(cost)
        mincost = [cost[0],cost[1]]
        for i in range(len(cost)-2):
            mincost[0], mincost[1] = mincost[1], min(mincost)+cost[i+2]
        return min(mincost)
        