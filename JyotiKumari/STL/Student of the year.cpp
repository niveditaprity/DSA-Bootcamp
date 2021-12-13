bool compare(pair<string,int> a1,pair<string,int> a2){
    if(a1.second>a2.second){
        return 1;
    }else if(a1.second==a2.second){
        if(a1.first<a2.first){
            return 1;
        }else{
            return 0;
        }
    }
    return 0;
}
vector<pair<string, int>> sortMarks(vector<pair<string, int>> v, int N){
    
    
    //Complete the code and return the sorted vector
    sort(v.begin(),v.end(),compare);
    return v;
}