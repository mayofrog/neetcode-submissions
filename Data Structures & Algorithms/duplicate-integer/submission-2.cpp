class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> H(0);
        for (int i = 0; i<n; i++){
            if(H[nums[i]] != 0)
                return true;
            H[nums[i]]++;
        }
        return false;
    }
};