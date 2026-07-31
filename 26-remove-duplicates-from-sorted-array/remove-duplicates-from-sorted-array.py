class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)

        nums = [nums.pop(i) for i in range (
            n - 1, 0, -1) if nums[i] ==
            nums[i - 1]]

        return n - len(nums)