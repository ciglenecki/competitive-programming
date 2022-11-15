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

int range_sum(int a, int b, std::vector<int> &is_workday_prefix_sum) {
    // caculated number of holidays
    if (a == 0) {
        return is_workday_prefix_sum[b];
    } else {
        return is_workday_prefix_sum[b] - is_workday_prefix_sum[a - 1];
    }
}

int solve(int v, int n, std::vector<int> &is_holiday, int free_days, std::vector<int> &is_workday_prefix_sum) {
    if (v == -1) return 0;
    dbg("=== SOLVE");
    dbg("vacation:", v);
    dbg("free_days", free_days);
    int free_days_int1, sum, new_sum;
    for (int i = 0; i < n - (v * 2); i++) {  // intreval 1
        dbg("Start of intervalA: ", i);
        dbg("End of intervalA: ", i + v - 1);

        sum = range_sum(i, i + v - 1, is_workday_prefix_sum);
        if (sum > free_days) {
            dbg("cont outer");
            continue;
        }
        dbg("Sum of int1", sum);

        for (int i2 = i + v; i2 <= n - v; i2++) {  // interval 2 moving head

            dbg("Start of intervalB", i2);
            dbg("End of intervalB", i2 + v - 1);

            new_sum = (range_sum(i2, i2 + v - 1, is_workday_prefix_sum));
            dbg("Sum of intB: ", new_sum);
            new_sum = new_sum + sum;
            dbg("Sum of in1 + intB: ", new_sum);
            if (new_sum <= free_days) {
                dbg("ret", v);
                return v;
            }
        }
    }
    dbg("ret", -1);
    return -1;
}

// https://stackoverflow.com/questions/28504835/c-11-binary-search-and-lambda-function-use-case

int main() {
    dbg();
    dbg("=== NEW TASK");
    dbg();
    // n i m (0 ≤ m ≤ n ≤ 5000),
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m, tmp, s, tmp_s, max_holiday, counter;
    cin >> n;
    cin >> m;

    std::vector<int> is_holiday(n);  // [0, 1, 1 ,1, 0, 0, 0, 0, 0, 0]
    std::vector<int> vacation_map;   // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    std::vector<int> is_workday_prefix_sum(n);
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        dbg("tmp", tmp);
        is_holiday[tmp] = 1;
    }
    cin >> s;

    if (m == 0) {
        cout << int(s / 2);
    }

    // if (s == 0) {
    //     std::vector<int> sums;

    //     int max = 0, counter = 0;
    //     for (int i = 0; i < n; i++) {
    //         if (is_holiday[i] == 0) {
    //             counter++;
    //         } else {
    //             sums.push_back(counter);
    //             counter = 0;
    //         }
    //     }
    //     sort(sums.begin(), sums.end(), std::greater<int>());

    //     cout << max;
    // }

    for (int i = 1; i <= n / 2; i++) {
        vacation_map.push_back(i);
    }

    dbg("is_holidat", is_holiday);
    dbg("vacation_map", vacation_map);

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            is_workday_prefix_sum[i] = 1 - is_holiday[0];
        } else {
            is_workday_prefix_sum[i] = is_workday_prefix_sum[i - 1] + (1 - is_holiday[i]);
        }
    }
    dbg("is_workday_prefix_sum", is_workday_prefix_sum);

    auto comp = [&](int v1, int v2) -> bool {
        int sv1, sv2;
        dbg("");
        dbg("Comparing v1, v2", v1, v2);
        sv1 = solve(v1, n, is_holiday, s, is_workday_prefix_sum);
        dbg("solve1", sv1);
        sv2 = solve(v2, n, is_holiday, s, is_workday_prefix_sum);
        dbg("solve2", sv2);

        return sv1 > sv2;
    };

    std::vector<int>::iterator low;
    low = lower_bound(vacation_map.begin(), vacation_map.end(), -1, comp);
    cout << (vacation_map[low - vacation_map.begin() - 1]);
}