/*

https://codeforces.com/group/zlRFu4TNaV/contest/405529/problem/B

Idea:

there are two approaches.
The first is to find the hero who will surely beat the dragon and the caculate the how many coins we need to defend against the dragon.
The second is to find the hero who almost beats the dragon, give him the needed coins, and give the coins to the defense (if needed).

The soltion is the approach which requires less coins.
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
    std::vector<ll> people_atk;

    ll tmp, atk, def, total_sum = 0;
    int num_people, num_dragons, hero_killer, almost_hero_killer, counter;

    cin >> num_people;
    counter = num_people;

    while (counter--) {
        cin >> tmp;
        people_atk.push_back(tmp);
        total_sum += tmp;
    }
    cin >> num_dragons;

    sort(people_atk.begin(), people_atk.end());

    dbg();
    dbg("Number of people:", people_atk.size());
    dbg("Number of dragons:", num_dragons);
    dbg("People", people_atk);
    dbg();

    for (int i = 0; i < num_dragons; i++) {
        ll coins = 3e18 + 1;
        ll diff = 0;

        cin >> def;
        cin >> atk;
        dbg("=== case", i);
        dbg("Dragon (def", def, ") (atk", atk, ")");
        dbg("Heroes", people_atk);

        hero_killer = lower_bound(people_atk.begin(), people_atk.end(), def) - people_atk.begin();
        almost_hero_killer = (hero_killer > 0) ? hero_killer - 1 : -1;

        if (almost_hero_killer > -1) {                                             // dragon guy is not the lowest one
            diff = max(0ll, def - people_atk[almost_hero_killer]);                 // difference between attacker and dragon's defense
            diff += max(0ll, atk - (total_sum - people_atk[almost_hero_killer]));  // difference between defenders and dragon's attack
            coins = min(coins, diff);
        }

        if (hero_killer < people_atk.size()) {                              // i still don't understand why need this condition
            diff = max(0ll, def - people_atk[hero_killer]);                 // difference between attacker and dragon's defense
            diff += max(0ll, atk - (total_sum - people_atk[hero_killer]));  // difference between defenders and dragon's attack
            coins = min(coins, (max(0ll, diff)));
        }

        cout << coins << "\n";
        dbg("Coins:", coins, "\n");
    }

    return 0;
}