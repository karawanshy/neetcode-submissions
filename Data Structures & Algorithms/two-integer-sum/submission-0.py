class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in unique:
                return [unique[complement], i]
            
            unique[num] = i

        return unique