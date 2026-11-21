class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            targetNum=target - nums[i]
            print(f"round{i}")
            print(targetNum)
            if targetNum in nums[i+1:]: 
                print("in")
                return [i, nums.index(targetNum, i+1)]

        