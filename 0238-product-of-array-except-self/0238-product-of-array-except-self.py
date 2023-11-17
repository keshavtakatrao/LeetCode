class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        
        left_prod = 1
        for i in range(0,n):
            result[i] *= left_prod
            left_prod *= nums[i]
            
        right_prod = 1
        for i in range(n-1,-1,-1):
            result[i] *= right_prod
            right_prod *= nums[i]
            
        return result