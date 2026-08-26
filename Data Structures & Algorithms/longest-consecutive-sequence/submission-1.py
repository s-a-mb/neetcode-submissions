class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        my_set = set()

        cur_seq = max_seq = 1

        for num in nums:

            my_set.add(num)

        my_arr = []

        for item in my_set:
            my_arr.append(item)

        my_arr.sort()

        for i in range(len(my_arr) - 1):
            if my_arr[i] + 1 == my_arr[i + 1]:
                cur_seq += 1
                max_seq = max(cur_seq, max_seq)
            else:
                cur_seq = 1
    

        
        
        return max_seq
