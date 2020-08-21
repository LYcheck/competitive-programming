import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sums = new HashMap<Integer, Integer>();
        int[] result = new int[]{0,0};
        
        for(int a = 0; a < nums.length; a++){
            int num = nums[a];
            int numNeeded = target - num;
            
            if(sums.containsKey(numNeeded)){
                result[0] = sums.get(numNeeded);
                result[1] = a;
                
                return result;
            }
            sums.put(num, a);
        }
        return result;
    }
}