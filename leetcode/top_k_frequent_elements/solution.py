class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]
