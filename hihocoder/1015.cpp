#include <iostream>
#include <string>

using namespace std;
int main() {
    int n;
    cin>>n;
    while(n--) {
        string S, W;
        int result=0;
        cin >> W;
        cin >> S;

        int *next = new int[S.length()];
        int i=0,j=-1;
        next[0] = -1;
        while(i<S.length()-1){
            if(j==-1 or S[i]==S[j]){
                ++i;
                ++j;
                next[i]=j;
            }else{
                j=next[j];
            }
        }

        i=0;j=0;
        while(i<S.length() and j<W.length()){
            if(S[i]==W[j]){
                ++i;
                ++j;
            }else{
                j=next[j];
                if(j==-1){
                    j=0;
                    ++i;
                }
            }

            if(j==W.length()){
                j=next[j];
                if(j==-1){
                    j=0;
                    ++i;
                }
                result+=1;
            }
        }

        cout<<result<<endl;
    }
}