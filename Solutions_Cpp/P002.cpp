#include <iostream>
using namespace std;

int main(){
	int b_fib=1, a_fib=2, sum=0;
	while(a_fib<4000000){
		if(a_fib%2==0) sum+=a_fib;
		a_fib += b_fib;
		b_fib = a_fib - b_fib;
	}
	cout << sum << endl;
	return 0;
}
