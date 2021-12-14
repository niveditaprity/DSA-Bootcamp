void swap(string a, string b){
    string temp;
    temp = a;
    a= b;
    b = temp;
}

string reverseWord(string str){
    
  //Your code here
  int len = str.size();
   for (int i = 0; i < len/2; i++)  
    {  
        // temp variable use to temporary hold the string  
        swap(str[i],str[len-i-1]);
    }  
  return str;
}