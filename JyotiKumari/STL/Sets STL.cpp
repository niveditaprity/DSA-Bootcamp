#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,q,val;
    cin>>n;
    set<int>s;
    for(int i=0; i<n; i++){
        cin>>q>>val;
        if(q==1){
            s.insert(val);
        }
        else if(q==2){
            s.erase(val);
        }
        else{
            set<int>::iterator itr=s.find(val); 
            if(itr!=s.end())
                cout<<"Yes"<<endl;
            else {
                cout<<"No"<<endl;
            }
        }
    }  
    return 0;
}



