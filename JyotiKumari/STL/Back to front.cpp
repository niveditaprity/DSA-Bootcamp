void reverseIterator(vector<int>::reverse_iterator it1, vector<int>::reverse_iterator it2){
    
    // Your code here
    while(it1!=it2){
        cout<<*it1<<" ";
        it1++;
    }
    cout<<endl;
    
}