class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap ={}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [i,numMap.get(diff)]

            numMap[num] = i

        return [] 