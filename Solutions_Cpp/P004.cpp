#include <iostream>
#include <string>
using namespace std;

bool is_palindrome(long long a){
	string string_a = to_string(a);
	int l=0, r=string_a.size()-1;
	while(l<=r){
		if(string_a[l++]!=string_a[r--]) return false;
	}
	return true;
}

int main(){
	long long max=0;
	for(int i=100; i<=999; i++){
		for(int j=i; j<=999; j++){
			if(is_palindrome(i*j) && i*j>max) max = i*j; 
		}
	}
	cout << max << endl;
	return 0;
}
