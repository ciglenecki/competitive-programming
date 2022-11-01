#include <bits/stdc++.h>

#include <map>
#include <set>

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

int my_is_prime(std::vector<bool> &primes, int n) {
    // try to find the divider within the known primes
    for (int i = 2; i < primes.size(); i++) {
        if (n % i == 0) {
            dbg("N ", n, " is not prime because its divisible with prearray element ", i, "\n");
            return -1;
        }
    }

    // continue building the prime list until you reach sqrt(n)
    int curr = primes.size() + 1;
    bool is_curr_prime;

    while (curr * curr <= n) {
        is_curr_prime = true;

        for (int i = 2; i < primes.size() && i * i < curr; i++) {
            if (curr % i == 0) {
                dbg("New number ", curr, " is not prime because it's divisible by ", i, "\n");
                is_curr_prime = false;
                break;
            }
        }

        // add the true/false value to the i-th place in the prime array
        primes.push_back(is_curr_prime);

        // check if the new prime is divider of n
        if (is_curr_prime && (n % curr == 0)) {
            dbg("N ", n, " is not prime because it's divisible with curr ", curr, "\n");
            return -1;
        }

        curr++;
    }
    // all prime numbers up to sqrt(n) were checked, n is a prime number.
    return n;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int tc, n, sum, prime_number;

    cin >> tc;
    std::map<int, int> cache = {};
    std::vector<bool> primes;
    std::set<int> primes_set;

    primes.push_back(false);  // 0
    primes.push_back(false);  // 1
    primes.push_back(true);   // 2
    primes.push_back(true);   // 3

    for (int t = 1; t <= tc; t++) {
        dbg("=== Checking number", n, "===\n");

        cin >> n;

        prime_number = 2;
        while (prime_number < primes.size()) {
            sum = prime_number + n;

            if (sum < primes.size() && primes[sum]) {
                dbg("Sum ", sum, " is prime, found it in the primes array\n");
                break;
            }

            if (my_is_prime(primes, sum) == -1) {
                cout << prime_number << "\n";
                break;
            };

            prime_number++;
        }
    }
}