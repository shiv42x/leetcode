class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counter = {}

        # for num in nums:
        #     if num not in counter:
        #         counter[num] = 1
        #     else:
        #         counter[num] += 1
        
        # for key in counter.keys():
        #     if counter[key] == 1:
        #         return key

        accum = 0
        
        # x ^ x = 0
        # 0 ^ x = x 
        # the idea is, every pair of numbers 'cancel' out to 0, except the single number! 

        for num in nums:
            accum = accum ^ num
       
        return accum