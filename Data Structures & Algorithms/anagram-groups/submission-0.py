class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedHash = {}

        for str in strs:
            sortedStr = ''.join(sorted(str))

            if sortedStr in sortedHash:
                sortedHash[sortedStr].append(str)
            else:
                sortedHash[sortedStr] = [str]

        return list(sortedHash.values())