#include <iostream>
using namespace std;

int gcd(int a, int b){
	if(b==0) return a;
	return gcd(b, a%b);
}

long long lcm(int a, int b){
	return a/gcd(a,b)*b;
}

int main(){
	long long ans=1;
	for(int i=1; i<=20; i++){
		ans=lcm(ans, i);

	}		
	cout << ans << endl;	
	return 0;
}
