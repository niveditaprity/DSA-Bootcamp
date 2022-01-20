class ProductOfNumbers {
public:
    vector<int>v;
    ProductOfNumbers() {
        
    }
    
    void add(int num) {
       if(num==0)
       {
           v.clear();
           return;
       }
        if(v.size()>=1)
        {
            v.push_back(v[v.size()-1]*num);
        }
        else
        {
            v.push_back(num);
        }
    }
    
    int getProduct(int k) {
        if(v.size()<k)
        {
            return 0;
        }
       else  if(v.size()==k)
        {
            return v[v.size()-1];
        }
        return v[v.size()-1]/v[v.size()-k-1];
        
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
