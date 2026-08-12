class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sliding window won't work because of possible -ve numbers

        intuition:  how many previous prefix sums equal (curr_sum - k)?
                    this gives us how many additional subarrays we can create by omitting those prefix sums

                    [..., x, ...]
                          ^
                     <--->curr_sum
                       |
                       |->  we store ~all~ prefix sums and their count in this area
                            then, we add to our final result how many previous prefix sums have value (curr_sum - k)
                            this way, when we remove that prefix sum from our curr_sum we get k:

                                                    (curr_sum) - (curr_sum - k)
                                                    (curr_sum - curr_sum) + k
                                                    0 + k
                            there could be multiple counts of the same prefix sum, so we track counts
                            an interesting property of using prefix sums is that:
                                n occurrences of a prefix sum indicate that n subarrays could be formed ending at the current index
        """      
        
        prefix_map = {0 : 1}
        curr_sum = 0
        n = len(nums)
        found_subarrays = 0

        for i in range(n):
            curr_sum += nums[i]

            # add # of subarrays whose prefix sum equals (curr_sum - k)
            found_subarrays += prefix_map.get(curr_sum - k, 0)

            # update prefix_map with (newly) found prefix_sum
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
    
        return found_subarrays
