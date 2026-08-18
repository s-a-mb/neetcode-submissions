class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # cost[index] is the cost of taking a step from itself towards the floor
        # can take a step to the next floor, or to the floor after that
        # can start at 0 or 1
        # check the next value, and the value after, compare, then decide which to go into


        checked = [-1] * len(cost)


        def recursion(i):
            if i >= len(cost):
                return 0
            
            if checked[i] != -1:
                return checked[i]

            checked[i] = cost[i] + min(recursion(i+1), recursion(i+2))
            return checked[i]

        return min(recursion(1), recursion(0))

            