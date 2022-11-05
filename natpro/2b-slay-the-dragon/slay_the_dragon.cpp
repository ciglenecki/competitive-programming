#include <bits/stdc++.h>
#include <stdlib.h> /* abs */

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

/*
Idea:
If we find a hero that can beat a dragon:
    Check if the rest of the team can defend aginst dragon, if they can't, caculate how many coins they need to defend against the dragon



Alternative: construct a team with a sum as close to dragons attack as possible.

    First, send the guy whose atck is closest to dragons def (abs) and pay him a difference

    Then pump up the rest of the team if needed



    The guy who is left out (prefereably the strongest) should get some coins

    start from the back of the sorted list. If cumulative sum of added heros + curr_hero_atk is less or eq than dragons atk then add that hero.

    If it's larager than reserve that hero for the attack.



*/
int my_lower_bound(std::vector<ll> vect, int x) {
    if (vect.size() == 0) {
        return -1;
    }
    if ((vect.size() == 1) || (x < vect.front())) {
        return 0;
    }
    if (x > vect.back()) {
        return vect.size();
    }
    int low = 0, high = vect.size() - 1, mid;

    while (low <= high) {
        // dbg("\n");

        mid = (low + high) / 2;
        // dbg("low", low);
        // dbg("mid", mid, x);
        // dbg("high", high);

        if (x == vect[mid]) {
            return mid;
        }

        else if (x > vect[mid]) {
            low = mid + 1;
        } else if (x < vect[mid]) {
            high = mid - 1;
        }
        // dbg("low", low);
        // dbg("mid", mid, x);
        // dbg("high", high);
    }
    return low;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    std::vector<ll> people_atk;

    ll tmp, atk, def, total_sum = 0;
    int num_people, num_dragons, dragon_guy_idx, almost_dragon_guy_idx;

    cin >> num_people;

    while (num_people--) {
        cin >> tmp;
        dbg("tmp", tmp);
        people_atk.push_back(tmp);
        total_sum += tmp;
        dbg(total_sum);
    }

    sort(people_atk.begin(), people_atk.end());

    cin >> num_dragons;
    dbg("Number of people:", people_atk.size());
    dbg("Number of dragons:", num_dragons);
    dbg("People", people_atk);

    for (int i = 0; i < num_dragons; i++) {
        ll coins = 3e18 + 1;
        ll diff = 0;

        cin >> def;
        cin >> atk;
        dbg("\n=== case", i, "\ndef", def, "atk", atk, "\n");
        dbg("Heroes", people_atk);

        dragon_guy_idx = lower_bound(people_atk.begin(), people_atk.end(), def) - people_atk.begin();
        // dragon_guy_idx = my_lower_bound(people_atk, def);
        almost_dragon_guy_idx = (dragon_guy_idx > 0) ? dragon_guy_idx - 1 : -1;

        dbg("hero+", dragon_guy_idx, "hero-", almost_dragon_guy_idx);

        if (almost_dragon_guy_idx > -1) {  // dragon guy is not the lowest one

            diff = max(0ll, def - people_atk[almost_dragon_guy_idx]);  // difference between attacker and dragon's defense
            dbg("diff 1", diff);
            diff += max(0ll, atk - (total_sum - people_atk[almost_dragon_guy_idx]));  // difference between defenders and dragon's attack
            dbg("diff 2", diff);
            coins = min(coins, diff);
            dbg("coins", coins);
        }

        if (dragon_guy_idx < people_atk.size()) {
            diff = max(0ll, def - people_atk[dragon_guy_idx]);  // difference between attacker and dragon's defense
            dbg("diff 3", diff);

            diff += max(0ll, atk - (total_sum - people_atk[dragon_guy_idx]));  // difference between defenders and dragon's attack
            dbg("diff 4", diff);

            coins = min(coins, (max(0ll, diff)));

            dbg("coins", coins);
        }
        cout << coins << "\n";
        dbg("\n\n");
    }

    return 0;
}