#include <algorithm>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.count(target - nums[i])) {
                // element found
                return vector<int>{m[target - nums[i]], i};
            }
            m[nums[i]] = i;
        }
        return vector<int>{nums[0], nums[1]};
    }
};
