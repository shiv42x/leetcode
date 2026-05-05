def productExceptSelf(self, nums: List[int]) -> List[int]:
#O(n) time, O(n) space
    result = []
    prefix = []
    postfix = []
    n = len(nums)

    product = 1
    for i in range(n):
        product *= nums[i]
        prefix.append(product)

    product = 1
    for i in range(n - 1, -1, -1):
        product *= nums[i]
        postfix.insert(0, product)

    for i in range(n):
        result.append((prefix[i - 1] if (i - 1 >= 0) else 1) * (postfix[i + 1] if (i + 1 < n) else 1))
    
    return result

    #O(n) time, O(1) space
    #use result array as buffer for prefix array
    result = [i] * (len(nums))
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res *= postfix
        postfix *= nums[i]
    return result