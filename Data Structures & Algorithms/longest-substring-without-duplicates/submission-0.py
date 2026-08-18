class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # need a dict that check is a letter is in the substring alread


        my_set = set()

        l = 0
        res = 0

        for r in range(len(s)):

            
            if s[r] in my_set:
                while s[l] != s[r]:
                    my_set.discard(s[l])
                    l+=1
                my_set.discard(s[l])
                l+=1
            
            
            my_set.add(s[r])
            res = max(res, r - l + 1)
        
        return res

            

