public class Solution {
    public int Search(int[] nums, int target) {
        int left =0;
        int right = nums.Length-1;
        int mid = 0;
        while(left <= right){
            mid = left + (right - left) / 2;
            // Console.WriteLine(mid);
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]<target){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        return -1;

        
    }
}
