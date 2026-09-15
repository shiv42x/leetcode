class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for j in range(len(ans)):
            i = 1 << 20
            while i > 0:
                if (j & i) != 0:
                    ans[j] += 1
                i = i // 2
        return ans
        