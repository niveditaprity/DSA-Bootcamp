#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    set<int> ss;
int Count;
cin >> Count;
for (int i=0; i<Count; ++i){
    int type, query;
    cin >> type >> query;
    switch (type){
        case 1:
            ss.insert(query);
            break;
        case 2:
            ss.erase(query);
            break;
        case 3:
            cout << (ss.find(query) == ss.end() ? "No" : "Yes") << endl;
            break;
    }
}  
return 0;
}






