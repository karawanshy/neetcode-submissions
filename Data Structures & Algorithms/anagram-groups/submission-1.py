class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord('a') - ord(ch)] += 1
            
            key = tuple(count)

            freqMap[key].append(s)

        return list(freqMap.values())

