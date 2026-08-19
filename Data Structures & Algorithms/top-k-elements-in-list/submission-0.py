class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # need to pull the k nums which have the highest frequency
        # as we iterate through the list, track the k element which is currenly the most frequent

        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        return sorted(my_dict, key=my_dict.get, reverse=True,)[:k]

