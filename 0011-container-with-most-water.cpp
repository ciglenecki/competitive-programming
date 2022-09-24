#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

//Given a string s, find the length of the longest substring without repeating characters.
class Solution {
   public:
    int maxArea(vector<int>& height) {
        int left = 0, maxArea = 0, area, h = 0;
        int right = height.size() - 1;
        while (left < right) {
            h = min(height[left], height[right]);
            area = h * (right - left);
            maxArea = max(area, maxArea);
            while (height[right] <= h && left < right) right--;
            while (height[left] <= h && left < right) left++;
        }
        return maxArea;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    // cin >> tc;
    Solution s;
    vector<int> input = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << s.maxArea(input) << "\n";
}
