class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        curLength = 0
        charDic = {}
        
        left,right=0,0
        while left <= right and right < len(s):
            frontChar=s[right]
            if (frontChar not in charDic) or (charDic[frontChar]<left):
                charDic[frontChar]=right
                curLength=right-left+1
                if curLength>maxLength: maxLength=curLength
                right +=1
            else:

                left = charDic[frontChar]+1
                charDic[frontChar]=right
                right+=1
                
                
        return maxLength


        