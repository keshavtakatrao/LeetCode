class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_seq = 1
        current_seq = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == (nums[i] - 1):
                current_seq += 1
            elif nums[i - 1] < nums[i]:  # Reset the sequence if not consecutive
                current_seq = 1

            max_seq = max(max_seq, current_seq)

        return max_seq