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

int sol = 0;
std::vector<int> niz = {0, 5, 3, 1, 2, 1, 3};
std::vector<int> dp;
std::vector<int> najmanji;
int x;
const int MAXN = 6;
int n;
int mod = 1e9 + 7;
int memo[MAXN];

int solve(int ostalo) {
    dbg("ostalo", ostalo);
    if (ostalo == 0) return 0;
    if (ostalo == 1) return 1;
    if (memo[ostalo] != -1) return memo[ostalo];
    return memo[ostalo] = (solve(ostalo - 1) + solve(ostalo - 2));
}

int main() {
    memset(memo, -1, sizeof memo);
    n = 4;
    cout << solve(n);
    return 0;
}