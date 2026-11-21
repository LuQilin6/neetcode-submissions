class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDic = defaultdict(list)
        for word in strs:
            wordFreq = [0]*26
            for letter in word: wordFreq[ord(letter)-ord('a')]+=1
            anagramDic[tuple(wordFreq)].append(word)
        return list(anagramDic.values())
        