class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 0
            map[i]+=1
            if map[i] > 1:
                return True
        return False
        