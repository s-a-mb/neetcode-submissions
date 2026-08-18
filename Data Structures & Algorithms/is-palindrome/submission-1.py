class Solution:
    def isPalindrome(self, s: str) -> bool:

        # true is palindrome

        #if aplhanum, pass to another stack/array
        #convert uppercase to lowercase

        # evalute len, go to midpoint, iterate through both left and right until finding either the end or a mismatch

        arr = []
        
        for letter in s:
            if letter.isalnum():
                arr.append(letter.lower())

        print(arr)
        
        length = len(arr)

        r = length - 1
        l = 0
        while l <= r:
            if arr[l] != arr[r]:
                return False
            
            r -= 1
            l += 1
        

        return True

        