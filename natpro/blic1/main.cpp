#include <bits/stdc++.h>

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
const int INT_INF = 1e6;

int range_sum(int a, int b, std::vector<int> &workday_prefix_sum) {
    // caculated number of holidays
    if (a == 0) {
        return workday_prefix_sum[b];
    } else {
        return workday_prefix_sum[b] - workday_prefix_sum[a - 1];
    }
}

int solve(int v, int n, int s, std::vector<int> &workday_prefix_sum) {
    if (v == INT_INF) return INT_INF;
    /*
        v: length of vacation
        n: number of year days+
        s: number of free days
    */

    int sum;
    for (int i = 0; i <= n - (v * 2); i++) {  // intreval 1

        sum = range_sum(i, i + v - 1, workday_prefix_sum);
        if (sum > s) {  // stop because the sum is alreaday larger than number of free days
            continue;
        }

        for (int i2 = i + v; i2 <= n - v; i2++) {  // interval 2 moving head
            if (sum + range_sum(i2, i2 + v - 1, workday_prefix_sum) <= s) {
                return v;
            }
        }
    }

    return INT_INF;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m, tmp, s;
    cin >> n;
    cin >> m;

    std::vector<int> vacation_lengths;  // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    std::vector<int> workday_prefix_sum(n, 1);

    // parse holidays, set to 0 because workday is 1 (default)
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        workday_prefix_sum[tmp - 1] = 0;
    }

    for (int i = 1; i < n; i++) {
        workday_prefix_sum[i] = workday_prefix_sum[i - 1] + workday_prefix_sum[i];
    }

    cin >> s;

    if (m == 0) {
        cout << int(s / 2);
        return 0;
    }

    // create a list of vacation lenghts we want to check
    for (int i = 1; i <= n / 2; i++) {
        vacation_lengths.push_back(i);
    }

    auto comp = [&](int v1, int v2) -> bool {
        int sv1, sv2;
        sv1 = solve(v1, n, s, workday_prefix_sum);
        sv2 = solve(v2, n, s, workday_prefix_sum);

        return sv1 < sv2;
    };

    std::vector<int>::iterator low;
    low = lower_bound(vacation_lengths.begin(), vacation_lengths.end(), INT_INF, comp);

    if (low == vacation_lengths.begin()) {  // no solution found so Ivan can't take a vacation
        cout << 0;
    } else {
        cout << (vacation_lengths[low - vacation_lengths.begin() - 1]);
    }
}