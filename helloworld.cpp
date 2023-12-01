#include<iostream>
using namespace std;
int main() {
    int n;
    string alpha ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '};
    string word = {"HELLO WORLD"};
    string res;

    for(int i=0;i<word.size();i++)
    {
        for(int j=0;j<=alpha.size();j++)
        {
            cout<<res<<alpha[j]<<endl;
            if(word[i]==alpha[j]){
                res=res+alpha[j];
                break;
            }
        
        }
    }
}
