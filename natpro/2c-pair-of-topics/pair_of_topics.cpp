/*

https://codeforces.com/group/zlRFu4TNaV/contest/405529/problem/C
Idea:

*/

#include <bits/stdc++.h>
#include <stdlib.h>

#include <vector>
using namespace std;

template <typename A, typename B>
ostream &operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template <typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type>
ostream &operator<<(ostream &os, const T_container &v) {
    os << '{';
    string sep;
    for (const T &x : v) os << sep << x, sep = ", ";
    return os << '}';
}
void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) {
    cerr << ' ' << H;
    dbg_out(T...);
}
#ifdef DEBUG
#define dbg(...) dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, tmp, elem_idx, sum = 0, finding;
    cin >> n;
    std::vector<int> arr, arr_ind;
    std::vector<int>::iterator element, zero_up;

    dbg("Test", n);
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        dbg(tmp);
        arr.push_back(tmp);
        arr_ind.push_back(i);
    }
    dbg(arr);
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        arr[i] -= tmp;
    }

    sort(arr.begin(), arr.end());
    zero_up = upper_bound(arr.begin(), arr.end(), 0);
    dbg(arr);
    for (int i = 0; i < n; i++) {
        // if (arr[i] >= 0) {
        //     sum += arr.size() - i;
        //     break;
        // }

        if (arr[i] < 0) {
            element = lower_bound(arr.begin() + i - 1, arr.end(), 0 - arr[i] + 1);
        } else if (arr[i] == 0) {
            element = zero_up;
        } else {
            // can be the same number
            element = arr.begin() + i + 1;
        }

        elem_idx = element - arr.begin();
        tmp = arr.size() - elem_idx;
        dbg("element", arr[i], "i:", i, "idx", elem_idx);
        dbg("tmp", tmp);
        dbg("");
        sum += tmp;
    }
    cout << sum;
}