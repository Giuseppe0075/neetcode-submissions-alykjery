class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_in_pile = max(piles)

        def solve(l,r):
            k = int((l+r)/2)
            if l == r:
                return k
            t = 0
            for p in piles:
                t += int(p/k)
                t += 1 if p%k > 0 else 0
            if t <= h:
                return solve(l,k)
            elif t > h:
                return solve(k+1,r)
        
        return solve(1, max_in_pile)
        