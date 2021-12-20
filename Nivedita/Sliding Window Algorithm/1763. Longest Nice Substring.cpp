class Solution {
public:
    bool isNice(string s)
    {
        for(char &x:s)
        {
            if(isupper(x)&&s.find(tolower(x)) == string::npos)
            {
                
                    return false;
            }
            else if(islower(x)&&s.find(toupper(x))==string::npos)
            {
                return false;
            }
        }
        return true;
    }
    string longestNiceSubstring(string s) {
      string ans="";
        
        
        for(int i=0;i<s.size();i++){
            string tmp="";
            tmp+=s[i];
            for(int j=i + 1;j<s.size();j++){
                tmp+=s[j];
                if(isNice(tmp)){
                    if(ans.size()<tmp.size()){
                        ans=tmp;
                    }
            
            }
        }
        
    }
         return ans;  
    }
};
