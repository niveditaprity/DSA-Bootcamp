class Solution {
public:
    bool checkValidString(string s) {
      int ast=0,opened=0,closed=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='*')
            {
                ast++;
            }
            else if(s[i]=='(')
            {
                opened++;
            }
            else
            {
                closed++;
            }
            if(closed>ast+opened)
            {
                return false;
            }
        }
        ast=0,opened=0,closed=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='*')
            {
                ast++;
            }
            else if(s[i]==')')
            {
                closed++;
            }
            else
            {
                opened++;
            }
            if(closed+ast<opened)
            {
                return false;
            }
        }
        return true;
    }
};
