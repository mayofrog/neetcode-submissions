class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        unordered_map<int, int> M;

        for(i = 0;i<nums.size(); i++){
            if(M.contains(target-nums[i]))
                return {M[target-nums[i]],i};
            M[nums[i]] = i;
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