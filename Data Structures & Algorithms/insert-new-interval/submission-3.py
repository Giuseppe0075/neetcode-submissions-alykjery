class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def overlaps(int1, int2):
            if int1[0] <= int2[0] <= int1[1] or int1[0] <= int2[1] <= int1[1]:
                return True
            if int2[0] <= int1[0] <= int2[1] or int2[0] <= int1[1] <= int2[1]:
                return True
            return False
        
        i = 0
        while intervals and i < len(intervals):
            if overlaps(intervals[i], newInterval):
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
                intervals.pop(i)
            else:
                i+=1
                
        n = len(intervals)
        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                return intervals
        intervals.append(newInterval)
        return intervals

