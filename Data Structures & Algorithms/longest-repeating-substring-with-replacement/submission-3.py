class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        maxLen=0
        cnt=Counter()
        # rep=0
        
        while left <= right and right<len(s):
            cnt[s[right]]+=1
            curLen=right-left+1
            right +=1 
            while (curLen-max(cnt.values()))>k: #exceed max replacement
                cnt[s[left]]-=1
                left+=1 
                curLen-=1
            maxLen = max(maxLen, curLen)
        return maxLen
                
        

        #xxyaxxx
        #a[bbb]
        #dic[a]=1
        # while left <= right and right<len(s):
        #     if s[left]==s[right]:
        #         maxLen = max(maxLen, right-left+1)
        #         right+=1
        #     else:
        #         if rep==0: nextLeft=right
        #         if rep<k: 
        #             rep+=1
        #             maxLen = max(maxLen, right-left+1)
        #             right+=1
        #         else:
        #             left, right = nextLeft, nextLeft
        #             rep=0
        #     # print(f"left: {left}, right: {right}")

        # return maxLen
                   


