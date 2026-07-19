class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in s:
            if i not in map:
                map[i] = 0
            map[i]+=1

        for i in t:
            if i not in map:
                return False
            map[i]-=1

        for i in map:
            if map[i] != 0:
                return False
        return True        
        