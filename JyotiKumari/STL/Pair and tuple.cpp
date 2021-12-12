#include <bits/stdc++.h>
pair<int, int> findMaxMin(vector<int> &A){
    // First value of pair will be Maximum of array A and second will be Minimum of array A
    int max,min;
    max = *max_element(A.begin(), A.end());
    min = *min_element(A.begin(), A.end());
    pair<int, int>p; 
    p.first = max;
    p.second = min;
    return p;
}

tuple<int, int, int> compute(vector<int> &A){
    // First value of tuple will be sum of array A
    // Second value of tuple will be sum of even values in array A 
    // Third value of tuple will be sum of odd values in array A
    int Sum_of_odd=0,sum_of_even=0;
    for(int i=0;i<A.size();i++){
        if(A[i]%2==0){
            sum_of_even+=A[i];
        }
        else{
            Sum_of_odd+=A[i];
        }
    }
    tuple<int,int,int>t;
    get<0>(t) = sum_of_even+Sum_of_odd;
    get<1>(t) = sum_of_even;
    get<2>(t) = Sum_of_odd;
    return t;
}