class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l]+ numbers[r]
            if  sum > target: 
                r-=1
            elif sum < target:
                l+=1
            else:
                return [l+1,r+1]

            
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in numbers[i+1:]: return [i+1, numbers.index(diff,i+1)+1]
        
