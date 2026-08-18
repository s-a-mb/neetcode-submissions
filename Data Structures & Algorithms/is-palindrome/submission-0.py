class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = ''

        for letters in s:
            if letters.isalnum():
                s2 += letters.lower()


        l = 0
        r = len(s2) - 1
        valid = True

        while l < r:
            if s2[l] != s2[r]:
                valid = False
                break
            l += 1
            r -= 1
        
        return valid
        