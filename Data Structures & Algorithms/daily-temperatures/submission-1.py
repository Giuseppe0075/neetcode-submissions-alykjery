class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        n = len(temperatures)
        for i in reversed(range(n)):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            days = stack[-1][1] - i if stack else 0
            res.insert(0,days)
            stack.append([temperatures[i],i])
        return res
#stack = [[100,8],[76,7],[46,6]]
#res = [1,1,0,0]
#46,6