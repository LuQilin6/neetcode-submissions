class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storeMap = {}
        for n in nums:
            if n in storeMap: return True
            storeMap[n]=1

        return False