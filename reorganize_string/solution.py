class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-freq, char] for char, freq in count.items()]
        heapq.heapify(max_heap)

        result = ""
        on_hold = None
        while max_heap or on_hold:
            if on_hold and not max_heap:
                return ""

            cnt, char = heapq.heappop(max_heap)
            result += char
            cnt += 1

            if on_hold:
                heapq.heappush(max_heap, on_hold)
                on_hold = None

            if cnt != 0:
                on_hold = [cnt, char]

        return result