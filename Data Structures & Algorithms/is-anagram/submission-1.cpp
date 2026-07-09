class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int m = t.size();
        int arr1[250] = {0};
        int arr2[250] = {0};
        if(n != m) return false;
        for(int i = 0; i<n; i++){
            arr1[s[i]]++;
            arr2[t[i]]++;
        }
        for(int i = 0; i<250; i++){
            if(arr1[i] != arr2[i])
                return false;
        }
        return true;
    }
};
