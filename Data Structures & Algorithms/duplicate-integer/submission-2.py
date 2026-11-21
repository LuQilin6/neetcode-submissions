class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storeMap = set()
        for n in nums:
            if n in storeMap: return True
            storeMap.add(n)

        return False