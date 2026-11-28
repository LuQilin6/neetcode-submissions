class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        curLength = 0
        charDic = {}
        
        left,right=0,0
        while left <= right and right < len(s):
            
            if (s[right] not in charDic) or (charDic[s[right]]<left):
                charDic[s[right]]=right
                curLength=right-left+1
                if curLength>maxLength: maxLength=curLength
                right +=1
            else:

                left = charDic[s[right]]+1
                charDic[s[right]]=right
                right+=1
                
            
            # print(charDic)
            # print(f"left: {left}, right: {right}")
                
        return maxLength

        #abcdade
        #zxyzab

        