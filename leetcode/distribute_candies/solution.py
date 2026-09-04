class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType_set = set(candyType)
        return min(len(candyType_set), len(candyType) // 2)