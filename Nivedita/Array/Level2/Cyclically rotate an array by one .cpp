void rotate(int arr[], int n)
{
  int t = arr[n-1];
  int p;
  for(int i=0;i<n;i++)
  {
    swap(arr[i],arr[n-1]);
  }
}
