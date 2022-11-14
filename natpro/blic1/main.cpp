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
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
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

void solve() {
}

int main() {
    // n i m (0 ≤ m ≤ n ≤ 5000),
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m, tmp, s, tmp_s, max_holiday, counter;
    // cin >> n;
    // cin >> m;
    // int holidays[n], possible[n];

    // TODO HERE
    s = 2;
    n = 8;
    std::vector<int> holidays = {0, 1, 1, 0, 0, 1, 1, 1};
    std::vector<int> possible(n);

    // for (int i = 0; i <= m; i++) {
    //     cin >> tmp;
    //     holidays[i] = tmp;
    // }

    for (int i = 0; i < n; i++) {
        dbg("i", i, possible);
        dbg("holi", holidays);
        tmp_s = s;

        // decrement until we have no free days left
        // while (tmp_s < -1) {
        //     max_holiday = 0;
        //     if (possible[i] == 0) {
        //         tmp_s--;
        //     }
        //     max_holiday++;
        // }
        // possible[i] = max_holiday;

        // h = 2
        // [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        // __________
        //     ___________________________________________

        // h = 2
        // [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        // __________
        //     __________2
        //        _______
        //           ____
        //              __________________________________

        // [1, 0, 1 ,1 ,1, 0, 1, 1]
        //  _______________
        //     ___________________

        if (i == 0) {
            max_holiday = 0;
            counter = 0;
            // decrement until  we shave no free days left
            dbg("decrementing until we use all days");
            while (tmp_s > -1 && counter < n) {
                if (holidays[counter] == 0) {
                    tmp_s--;
                }
                counter++;
                max_holiday++;
            }

            possible[i] = max_holiday - 1;
            dbg(possible);
            continue;
        }

        if (i > 0) {
            max_holiday = possible[i - 1];
            counter = max_holiday;
            tmp_s = 0;

            // LEFT SIDE CHANGES

            if (holidays[i - 1] == 1 && holidays[i] == 0) {  // the previous day was holiday and today is work-day
                max_holiday--;
            }
            if (holidays[i - 1] == 1 && holidays[i] == 1) {  // previous day and today is holiday. that means that we have just one day less because we are still spending the same amount of time
                max_holiday--;
            }

            if (holidays[i - 1] == 0 && holidays[i] == 1) {
                dbg("jesi li prosao decko");
                tmp_s++;
                max_holiday--;
            }

            dbg(possible);
            dbg("counter", counter);
            dbg("max_holiday", max_holiday);

            dbg("finding free days on right side");
            while (tmp_s > -1 && counter < n) {
                if ((counter) < n && holidays[counter] == 0) {
                    dbg("decreasing because of zero at", counter);
                    tmp_s--;
                }

                counter++;
                max_holiday++;

                dbg("counter", counter);
                dbg("max_holiday", max_holiday);
                dbg("tmp_s", tmp_s);
            }
        }

        possible[i] = max_holiday;
        dbg(possible);
        dbg();
    }

    dbg(possible);
    cin >> s;
    // todo: mozemo li nekako doci do duljine?
    // idea: napravimo array koji sadrzi max duljinu puta za svaki dan i sortiram ju?

    // zamislimo da je zadana duljina i da moramo provjeriti je li mozemo za tu duljinu?
    // todo: binary search duljina putovanja umjesto for petlje

    for (int i = n / 2; i > 0; i--) {
        for (int j = 0; j < n; i++) {
        }
    }
}