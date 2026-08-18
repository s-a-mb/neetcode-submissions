class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # 2 bars create a container. find the container of the biggest size

        # the height of the container will be the smallest of the 2 bars

        #width of container will be the difference in indexes

        # if min(bar[l], bar[r]) * r-1 > current_area


        area = 0

        current_area = 0

        l = 0

        r = len(heights) -1

        while l < r:
            if min(heights[l], heights[r]) * (r-l) > area:
                area = min(heights[l], heights[r]) * (r-l)
            
            if heights[l] < heights[r]:
                l += 1
            
            else:
                r-=1
        
        return area



        