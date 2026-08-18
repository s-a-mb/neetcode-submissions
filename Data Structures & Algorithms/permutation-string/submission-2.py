class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # return true as soon as you find a permutation
        # otherwise return false

        s1_dict = dict()
        
        for letters in s1:
            if letters not in s1_dict:
                s1_dict[letters] = 1
            else:
                s1_dict[letters] += 1
        
        for slices in range(len(s2) - len(s1) + 1):
            s2_dict = dict()
            for letters in s2[slices:slices+len(s1)]:
                if letters not in s2_dict:
                    s2_dict[letters] = 1
                else:
                    s2_dict[letters] += 1
            
            if s1_dict == s2_dict:
                return True

        return False