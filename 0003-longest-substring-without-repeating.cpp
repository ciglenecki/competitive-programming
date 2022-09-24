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
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> m;
        int left = 0;
        int max_len = 0;
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (m.count(c)) {
                left = std::max(left, m[c] + 1);
            }
            m[c] = i;
            max_len = std::max(max_len, (i - left + 1));
        }
        return max_len;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    // cin >> tc;
    Solution s;
    string input = "abcabc";
    cout << s.lengthOfLongestSubstring(input) << "\n";
}
