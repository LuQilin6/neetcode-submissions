from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashS = Counter(s)
        hashT = Counter(t)
        if hashS == hashT: return True
        return False
