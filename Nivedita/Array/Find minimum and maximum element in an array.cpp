pair<long long, long long> getMinMax(long long arr[], int n) {
  pair<long long,long long>p;
  int max=arr[0],min=arr[0];
  for(int i=1;i<n;i++)
  {
      if(max<arr[i])
      {
          max=arr[i];
      }
      if(min>arr[i])
      {
         min=arr[i];
      }
  }
  p=make_pair(min,max);
  return p;
}
