class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDic = {}
        letterFreq = [0]*26
        for word in strs: #O(M)
            # nLength = len(n)
            # nCount = Counter(n) #O(N)
            for a in word: letterFreq[ord(a)-ord('a')]+=1
            # print(letterFreq)
            tag=''.join(str(letterFreq))
            # for l in letterFreq: tag.join(str(l))
            if tag in anagramDic: #O(M)
                anagramDic[tag].append(word)
            else: 
                anagramDic[tag] = [word]
            letterFreq = [0]*26

        #O(M*N)
        # print(anagramDic)
        result = []
        for _, v in anagramDic.items():#O(M)
            result.append(v)
        return result

        '''
        SET {{'A':2,'B':3}}
        '''