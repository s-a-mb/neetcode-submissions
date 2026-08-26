class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

       

        cur_seq = max_seq = 1

        my_set = set(nums)

        my_arr = list(my_set)

        my_arr.sort()

        for i in range(len(my_arr) - 1):
            if my_arr[i] + 1 == my_arr[i + 1]:
                cur_seq += 1
                max_seq = max(cur_seq, max_seq)
            else:
                cur_seq = 1
    

        
        
        return max_seq
