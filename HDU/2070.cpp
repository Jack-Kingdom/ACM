#include <iostream>
using namespace std;

__int64 fib(int n){
    __int64 a=0,b=1,c;
    while(n--){
    	c=a+b;
    	a=b;
    	b=c;
    }
    return a;
}

int main(){
	int n;
	while(cin>>n && n!=-1){
		cout<<fib(n)<<endl;
	}
	return 0;
}
