class Solution {
public:
    bool backspaceCompare(string S, string T) {
        string str="";
        string ptr="";
        for(int i=0;i<S.size();i++)
        {
            if(S[i]>='a'&&S[i]<='z')
            {
                str+=S[i];
            }
            else if(!str.empty())
            {
              str.pop_back();  
            }
        }
        for(int i=0;i<T.size();i++)
        {
            if(T[i]>='a'&&T[i]<='z')
            {
                ptr+=T[i];
            }
            else if(!ptr.empty())
            {
              ptr.pop_back();  
            }
        }
        if(str==ptr)
        {
            return true;
        }
        return false;
        
