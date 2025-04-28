class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, len(nums)):
            curr_num = nums[i]
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += curr_num
            max_sum = max(max_sum, curr_sum)

        return max_sum
        