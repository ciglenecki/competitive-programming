#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

template <typename T>
void print(T t) {
    std::cout << t << " ";
    std::cout << "\n";
}

template <typename T, typename... Args>
void print(T t, Args... args) {
    std::cout << t << " ";
    print(args...);
}

//Given a string s, find the length of the longest substring without repeating characters.

class Solution {
   public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>* smaller;
        vector<int>* larger;
        int cut_large, cut_small, left_small, left_large, right_small, right_large;
        double result;
        long long INF = 1e9;

        if (nums1.size() >= nums2.size()) {
            smaller = &nums2;
            larger = &nums1;
        } else {
            smaller = &nums1;
            larger = &nums2;
        }

        int smaller_size = (*smaller).size();
        int larger_size = (*larger).size();
        int total_size = smaller_size + larger_size;
        cut_small = (smaller_size) / 2;

        if (smaller_size == 0) {
            if (total_size % 2 == 0) {
                return (double)((*larger)[(larger_size - 1) / 2] + (*larger)[(larger_size / 2)]) / 2.;
            } else {
                return (*larger)[larger_size / 2];
            }
        }

        // print("\nsmaller");

        // for (int i = 0; i < smaller_size; i++) {
        //     cout << ((*smaller)[i]) << "  ";
        //     ;
        // }
        // print("");

        // print("\nlarger");
        // for (int i = 0; i < larger_size; i++) {
        //     cout << ((*larger)[i]) << "  ";
        // }
        // print("");
        // print("");

        while (cut_small <= smaller_size) {
            cut_large = (total_size + 1) / 2 - cut_small;
            // print("cut_small: ", cut_small, " cut_large: ", cut_large);
            // print("");

            // printf("%8s", "i: ");
            // for (int i = 0; i <= larger_size; i++) {
            //     printf("%4d", i);
            // }
            // print("");
            // printf("%10s", "----------");
            // for (int i = 0; i <= larger_size; i++) {
            //     printf("----");
            // }
            // print("");

            // printf("%10s", "smaller: ");

            // for (int i = 0; i <= smaller_size; i++) {
            //     if (i != smaller_size && i != cut_small) {
            //         printf("%4d", (*smaller)[i]);
            //     }

            //     if (i == smaller_size && i == cut_small) {
            //         printf(" | ");
            //     }

            //     if (i != smaller_size && i == cut_small) {
            //         printf(" |%2d", (*smaller)[i]);
            //     }
            // }
            // print("");
            // printf("%10s", "larger: ");

            // for (int i = 0; i <= larger_size; i++) {
            //     if (i != larger_size && i != cut_large) {
            //         printf("%4d", (*larger)[i]);
            //     }

            //     if (i == larger_size && i == cut_large) {
            //         printf(" | ");
            //     }

            //     if (i != larger_size && i == cut_large) {
            //         printf(" |%2d", (*larger)[i]);
            //     }
            // }
            // print("");
            // print("");

            // print("small i:", cut_small, " element: ", (*smaller)[cut_small]);
            // print("large i:", cut_large, " element: ", (*larger)[cut_large]);

            left_small = (cut_small == 0) ? -INF : (*smaller)[cut_small - 1];
            right_small = (cut_small == smaller_size) ? INF : (*smaller)[cut_small];
            left_large = (cut_large == 0) ? -INF : (*larger)[cut_large - 1];
            right_large = (cut_large == larger_size) ? INF : (*larger)[cut_large];

            // print("small:", left_small, right_small);
            // print("large:", left_large, right_large);

            if (left_large <= right_small && left_small <= right_large) {
                if (total_size % 2 == 0) {
                    int one = max(left_small, left_large);
                    int two = min(right_small, right_large);
                    // print("one: ", one, "two: ", two);
                    return (double)(one + two) / 2.;
                } else {
                    return max(left_large, left_small);
                }
            } else if (left_small >= right_large) {
                cut_small--;
            } else if (right_small < left_large) {
                cut_small++;
            }
            // print("cut_small: ", cut_small);
        }
        return result;
    }
};

int main() {
    ios_base::sync_with_stdio(true);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    // cin >> tc;
    Solution s;
    vector<int> i1 = {};
    vector<int> i2 = {2, 3};
    double result = s.findMedianSortedArrays(i1, i2);
    cout << result << "\n";
}
