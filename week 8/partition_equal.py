class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        target = Sum / 2
        dp = set()
        dp.add(0)
        for num in nums:
            new_dp = set()
            for curr in dp:
                if num + curr == target or curr == target:
                    return True
                new_dp.add(curr)
                new_dp.add(num + curr)
            dp = new_dp
        return False