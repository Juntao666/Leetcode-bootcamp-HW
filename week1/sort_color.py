class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p_0 = 0
        p_2 = n - 1
        curr = 0
        while curr <= p_2:
            curr_val = nums[curr]
            if curr_val == 2:
                nums[curr], nums[p_2] = nums[p_2], nums[curr]
                p_2 -= 1
            elif curr_val == 0:
                nums[curr], nums[p_0] = nums[p_0], nums[curr]
                p_0 += 1
                curr += 1
            else:
                curr += 1
            
        
