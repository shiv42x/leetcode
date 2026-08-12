class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1, 2], [1, 3], [1, 1]].sort()
        [[1, 1], [1, 2], [1, 3]]

        """
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:          
            previous_end = output[-1][1]
            if start <= previous_end:
                # then can merge
                output[-1][1] = max(previous_end, end)
            else:
                output.append([start, end])

        return output