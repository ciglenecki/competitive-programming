
// CPP program to illustrate
// std :: lower_bound
#include <bits/stdc++.h>
#include <stdlib.h>

#include <vector>
using namespace std;
// Driver code
int main() {
    // Input vector
    std::vector<int> v{-5, -5, 0, 0, 0, 10, 20, 30, 30, 30, 40, 50};

    // Print vector
    std::cout << "Vector contains :";
    std::vector<int>::iterator low1, low2, low3;

    low1 = std::upper_bound(v.begin(), v.end(), 0);
    low2 = std::lower_bound(v.begin(), v.end(), 35);
    low3 = std::lower_bound(v.begin(), v.end(), 55);

    // Printing the lower bounds
    std::cout
        << "\nlower_bound for element 30 at position : "
        << (low1 - v.begin());
    std::cout
        << "\nlower_bound for element 35 at position : "
        << (low2 - v.begin());
    std::cout
        << "\nlower_bound for element 55 at position : "
        << (low3 - v.begin());

    return 0;
}