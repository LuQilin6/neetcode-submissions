class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        maxLen=0
        cnt={}
        maxF=0
        
        while left <= right and right<len(s):
            frontChar=s[right]
            cnt[frontChar]=1+cnt.get(frontChar, 0)
            maxF=max(maxF, cnt[frontChar])
            curLen=right-left+1
            right +=1 
            while (curLen-maxF)>k: #exceed max replacement
                backChar=s[left]
                cnt[backChar]-=1
                maxF=max(maxF, cnt[backChar])
                left+=1 
                curLen-=1
            maxLen = max(maxLen, curLen)
        return maxLen