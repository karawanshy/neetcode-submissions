class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for ch in s:
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1
        
        for ch in t:
            if ch not in letters or letters[ch] == 0:
                return False
            
            letters[ch] -= 1
        
        for ch in letters:
            if letters[ch] != 0:
                return False

        return True