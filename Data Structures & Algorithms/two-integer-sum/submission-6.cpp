class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> M;

        for(int i = 0;i<nums.size(); i++){
            int a = target-nums[i];
            if(M.contains(a))
                return {M[a],i};
            M[nums[i]] = i;
        }
        return {};
    }
};