class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return 0
        from collections import Counter
        def top2(counter):
            most_common = counter.most_common(2)
            if len(most_common) == 1:
                most_common.append((None, 0))
            return most_common

        # counts of nums in odd and even indices
        odds = Counter(nums[1::2])
        evens = Counter(nums[::2])

        # top 2 so we can use 2nd most in case of ties
        (o1, o1_count), (o2, o2_count) = top2(odds)
        (e1, e1_count), (e2, e2_count) = top2(evens)

        if o1 != e1:
            return n - (o1_count + e1_count)
        else:
            return n - max(o1_count + e2_count, o2_count + e1_count) 