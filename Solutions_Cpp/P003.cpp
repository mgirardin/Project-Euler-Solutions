#include <iostream>
using namespace std;

int main(){
	long long num = 600851475143, ans;
	for(long long i=2;;){
		if(num <= i){
			break;
		}	
		else if(num%i==0){
			num/=i;	
		}
		else{
			i++;
		}
	}
	cout << num << endl;
	return 0;
}
