#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> adj;
    int a, b;
    string in, n;
    cin >> a;
    cin >> b;

    for(int i = 0; i < a; i++){
        cin >> in;
        adj.push_back(in);
    }
    for(int j = 0; j < b; j++){
        string n;
        cin >> n;
        
        for(auto &ele : adj){
            cout << ele << " as " << n << endl;
        }
    }
}