
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N; cin >> N;
    vector<int> arr(N);
    for (int k = 0; k < N; k++)
        cin >> arr[k];
    
    int Q; cin >> Q;
    while (Q--)
    {
        int val; cin >> val;
        auto it_lb = lower_bound(arr.begin(), arr.end(), val);
        auto it_ub = upper_bound(arr.begin(), arr.end(), val);
        if (it_lb == it_ub)
            cout << "No" << ' ' << it_ub-arr.begin()+1 << endl;
        else
            cout << "Yes" << ' ' << it_lb-arr.begin()+1 << endl;
    }
    
    return 0;
}
