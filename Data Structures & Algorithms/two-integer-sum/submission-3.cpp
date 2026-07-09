class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        unordered_map<int, int> M;

        for(i = 0;i<nums.size(); i++){
            if(M[target-nums[i]] != 0)
                return {M[target-nums[i]]-1,i};
            M[nums[i]] = i+1;
        }
        return {};
    }
};
 // while(i<j){
        //     int val = nums[i]+nums[j];
        //     if(val == target){
        //         return {i,j};
        //     }
        //     else if(val > target)
        //         j--;
        //     else
        //         i++;
        // }
        // return {};