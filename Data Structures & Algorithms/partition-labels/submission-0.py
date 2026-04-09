class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lastPosition = collections.defaultdict(int)

        #First setting
        for i in range(n):
            lastPosition[s[i]] = i
        
        l = 0
        ans = []
        iToArrive = 0
        for i in range(n):
            l += 1
            iToArrive = max(iToArrive,lastPosition[s[i]])
            if i == iToArrive:
                ans.append(l)
                l = 0
            
        return ans
        




        # xyxxyzbzbbisl
        # s:i
        # i_to_arrive: 10
        # h: {x:3, y:4, z:7, b:9, i:10, s:11, l:12}
        # ans = [5,5,1]