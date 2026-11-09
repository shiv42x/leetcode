class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    from typing import List
    ans = []
    used = [False] * len(nums)
    nums.sort() 

    def dfs(path: List[int]) -> None:
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      for i in range(len(nums)):
        if used[i]:
            continue

        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue

        used[i] = True
        path.append(nums[i])
        dfs(path)
        path.pop()
        used[i] = False

    dfs([])
    return ans