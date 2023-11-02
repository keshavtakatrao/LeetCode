class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        obj = defaultdict(int)
        
        for i in nums:
            obj[i] += 1
                
        obj = sorted(obj, key=lambda x: (-obj[x], x))
        
        return obj[:k]
        