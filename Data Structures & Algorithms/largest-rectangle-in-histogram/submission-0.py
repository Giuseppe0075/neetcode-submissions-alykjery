class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        s = [] #pair (index, height)
        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                area = (i-s[-1][0]) * s[-1][1]
                maxArea = max(maxArea, area)
                start = s[-1][0]
                s.pop()
            s.append([start,h])
        while s:
            area = (n-s[-1][0]) * s[-1][1]
            maxArea = max(maxArea, area)
            s.pop()
        return maxArea            