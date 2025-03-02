class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        res = []
        
        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
       
        return res
        