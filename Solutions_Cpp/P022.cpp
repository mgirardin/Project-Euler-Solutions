#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main(){
	vector<string> names;
	string word;
	ifstream name_file;
	long long sum = 0, name_val;
	name_file.open("P022_names.txt");
	//Storing every name of the txt file in the vector
	while(getline(name_file, word, ',') && word != ""){
		names.push_back(word.substr(1,word.size()-2));		
	}
	//Sorting list of names
	sort(names.begin(), names.end());
	//Calculating name value and multipling by its place in the list
	for(int i=0; i<names.size(); i++){
		name_val = 0;
		for(int j = 0; j<names[i].size(); j++){
			name_val+=(names[i][j]-'A'+1);
		}
		sum+=(name_val*(i+1));
	}
	cout << sum << endl;
	return 0;
}
