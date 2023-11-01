class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numset = set()

        for i in nums:
            if i in numset:
                return True
            else:
                numset.add(i)

        return False 
        