class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        if(nums.length == 0 || (nums[0] > target) || (nums[0] == target && nums.length == 1)) return 0;
        else if(nums[nums.length-1] < target) return nums.length;
        
        while(nums[i+1] < target){
            i++;
        }
        
        if(nums[i] == target) return i;
        return i+1;
    }
}