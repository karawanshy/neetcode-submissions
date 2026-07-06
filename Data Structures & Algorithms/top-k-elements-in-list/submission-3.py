class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencyArr = [[] for i in range(len(nums) + 1)]


        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            frequencyArr[cnt].append(num)

        res = []
        for i in range(len(frequencyArr) - 1, 0, -1):
            for num in frequencyArr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res