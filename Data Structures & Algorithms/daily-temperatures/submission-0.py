class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # build an array result that returns i values where i indicates how many days later compared to
        # temperatures[i] there is a warmer day

        result = []

        for i in range(len(temperatures)):
            dif = 0
            for j in range(i + 1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    dif = j-i
                    break
            result.append(dif)
        
        return result


