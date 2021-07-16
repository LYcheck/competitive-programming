class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        /*
        int countInd = 0;
        
        for(int x = 0; x < nums.size(); x++){
            for(int y = x; y < nums.size(); y++){
                unsigned int check = 1;
            
                int o = (nums[x] ^ nums[y]);
            
                while(check != 0){
                    if((check & o) == check) countInd++;
                    check <<= 1;
                }
            }
        }
        return countInd;
        */

        int tot = 0;
        unsigned int contrast = 1;
        int size = nums.size();

        while(contrast != 0){
            int count = 0;
            for(int i = 0; i < size; i++){
                if((nums[i] & contrast) == contrast) count++;
            }
            contrast <<= 1;
            tot += count * (size - count);
        }
        return tot;
    }
};