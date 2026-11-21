class Solution:
    def isPalindrome(self, s: str) -> bool:
        lenS = len(s)
        i = 0
        j = lenS-1
        s = s.lower()
        
        print(s)
        while i < j:
            print(s[i].isalpha())
            while (not s[i].isalpha() and not s[i].isdigit()) and i<j: i+=1
            while (not s[j].isalpha() and not s[j].isdigit()) and j>i: j-=1
            print(f"si: {s[i]}")
            print(f"sj: {s[j]}")
            if s[i]!=s[j] and i < j: return False
            i += 1
            j -= 1
        
        return True
        