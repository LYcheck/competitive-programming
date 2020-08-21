class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        
        for(int x = 1; x < nums.length; x++){
            if(nums[x] != nums[index]){
                index++;
                nums[index] = nums[x];
            }
        }
        return index + 1;
    }
}