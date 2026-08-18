class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l=total=res=0

        
        for r in range(len(arr)):

            total += arr[r]

            if r >= k - 1:
                if total / k >= threshold:
                    res += 1
                total -= arr[l]
                l+=1

        return res



            