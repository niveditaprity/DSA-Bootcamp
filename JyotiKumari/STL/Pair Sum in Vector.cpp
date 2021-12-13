void sum(vector<pair<int,int>>v)
{
    long long sum=0;
    //Your code 
    for(auto x:v){
        sum+=x.second;
    }
    cout<<sum;
    cout<<endl;
}