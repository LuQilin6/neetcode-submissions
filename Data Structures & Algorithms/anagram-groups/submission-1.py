class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDic = {}
        for n in strs:
            sortedN=''.join(sorted(n))
            if sortedN in anagramDic: 
                anagramDic[sortedN].append(n)
            else: 
                anagramDic[sortedN] = [n]

        result = []
        for k, v in anagramDic.items():
            result.append(v)
        return result

        