class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        cur =[]

        
        def dfs(j):

            if j >= len(s):
                res.append(cur.copy())
                return

            for i in range(j, len(s)):
                if self.isPali(s, j, i):
                    cur.append(s[j:i+1])
                    dfs(i + 1)
                    cur.pop()
        
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
                