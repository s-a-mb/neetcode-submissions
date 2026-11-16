class Solution:

    def encode(self, strs: List[str]) -> str:
        e_str = []

        for s in strs:
            e_str.append(str(len(s)))
            e_str.append('#')
            e_str.append(s)

        return "".join(e_str)

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res

