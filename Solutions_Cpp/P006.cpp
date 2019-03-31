#include <iostream>
using namespace std;

int main(){
	long long sum_squares, square_sum;
	sum_squares = 100*101*(201)/6;
	square_sum  = 100*100*101*101/4;
	cout << square_sum - sum_squares << endl;
	return 0;
}
