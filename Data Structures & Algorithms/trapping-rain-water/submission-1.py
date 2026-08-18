class Solution:
    def trap(self, height: List[int]) -> int:

        r, l = len(height) - 1, 0

        max_a, max_l, max_r = 0, height[l], height[r]

        # if r < l:
        # r++

        while l < r:
            if max_l > max_r:
                r -= 1
                max_r = max(max_r, height[r])
                max_a += max_r - height[r]
                
                
            else:
                l += 1
                max_l = max(max_l, height[l])
                max_a += max_l - height[l]
                

        return max_a
                

            
            


           


            
            
