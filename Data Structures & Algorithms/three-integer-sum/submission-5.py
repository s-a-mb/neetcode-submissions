class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # if i != j and i != k and j!=k
        # if nums[i] + nums[j] + nums[k] = 0

        # array of arrays
        # if above statements true, pass the values into and array, which then goes into an array

        res = []

        nums.sort()
        sum = 0
        


        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            if nums[i] == nums[i - 1] and i > 0:
                continue

            while j < k:

                sum = nums[i] + nums[j] + nums[k]

                #if sum == 0 and i != j and i != k and j!= k:
                 #   res.append([nums[1], nums[j], nums[k]])

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1


        return res
