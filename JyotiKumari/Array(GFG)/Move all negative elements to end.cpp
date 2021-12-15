class Solution{
    public:
    void segregateElements(int arr[],int n)
    {
        // Your code goes here
        int a[n],front=0,end=n-1,back=n-1;
        for(int i=0; i<n, end>=0; i++,end--){
            if(arr[i]>=0){
                a[front] = arr[i];
                front++;  
            }
            if(arr[end]<0){
                a[back] = arr[end];
                back--;
            }
        }
        for(int i=0; i<n; i++){
            arr[i] = a[i];
        }
    }
};