class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[w] = nums[r]
                w += 1 
        return w
