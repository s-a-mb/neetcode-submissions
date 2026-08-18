class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # find the max container size using two bars in a bar chart

        # min height of 2 bars * index difference gives max


        maxA = 0


        l = 0
        r = len(heights) - 1

        while l < r:
            cur = min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, cur)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxA
        