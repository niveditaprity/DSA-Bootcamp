class Solution {
public:
    string minRemoveToMakeValid(string s) {
       stack<pair<char,int>>st;
        
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]==')')
            {
                if(st.empty())
                {
                    st.push({s[i],i});
                }
                else
                {
                    if(st.top().first =='(' && s[i]==')')
                    {
                        st.pop();
                    }
                    else
                    {
                        st.push({s[i],i});
                    }
                }
            }
        }
        
        string str;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(st.size()>0 && st.top().second==i)
            {
                st.pop();
            }
            else
            {
                str+=s[i];
            }
        }
        reverse(str.begin(),str.end());
        return str;
       
    }
};
