class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        
        if len(piles) == h:
            return upper

        lower = math.ceil(sum(piles) / h)
        result = upper
        while lower <= upper:
            k = lower + (upper - lower) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            
            if hrs > h:
                lower = k + 1
            else:
                result = k
                upper = k - 1
        
        return result
