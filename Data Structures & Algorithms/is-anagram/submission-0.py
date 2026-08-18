class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        
        for letters in s:
            if letters not in dict1:
                dict1[letters] = 1
            else:
                dict1[letters] += 1
        
        for letters in t:
            if letters not in dict2:
                dict2[letters] = 1
            else:
                dict2[letters] += 1
        
        if dict1 == dict2:
            return True
        else:
            return False
            