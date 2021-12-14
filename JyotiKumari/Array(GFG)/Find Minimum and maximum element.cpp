pair<long long, long long> getMinMax(long long a[], int n) {
    pair<long long, long long>p;
    p.first = *min_element(a, a + n);
    p.second = *max_element(a, a + n);
    
    return p;
}