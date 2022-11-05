#include <bits/stdc++.h>

#include <vector>
using namespace std;

/*

idea- build staircase (sort) and the fill the staircase from the back

*/
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


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    std::vector<int> benches;
    // highest number, max(vector) + num_people

    int num_benches, num_people, tmp, max_people_on_single_bench;
    int j = -1;
    int range = 1;

    cin >> num_benches >> num_people;
    dbg("num_benches", num_benches, "num_people", num_people);
    for (int i = 0; i < num_benches; i++) {
        cin >> tmp;
        benches.push_back(tmp);
    }

    sort(benches.begin(), benches.end());
    max_people_on_single_bench = benches.back() + num_people;

    for (int i = 0; i < num_people; i++) {
        if (j == -1) {
            /*
            Imagine you have staircases which rise. Once the staircase reaches the same level as the right staircase you need to updated the range so that the range includes the new right staircase.

            However, you want to continue searching if there are more staircases at the same level, and include them too.
            */
            while ((range < num_benches) && benches.at(range - 1) >= benches.at(range)) {
                range++;
            }

            j = range - 1;
        }

        dbg(j, range);

        /*
        Start adding people at the end of the range.
        */
        benches.at(j) += 1;
        j--;
    }

    dbg(benches);

    cout << benches.back() << " " << max_people_on_single_bench;
}