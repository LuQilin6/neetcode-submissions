class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashS = Counter(s)
        for letter in t:
            if letter not in hashS or hashS[letter]==0: return False
            hashS[letter] -=1

        return True