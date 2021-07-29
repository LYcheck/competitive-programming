#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, sCount, tCount;
    sCount = tCount = 0;
    cin >> n;
    cin.ignore();
    
    for(int i = 0; i < n; i++){
        string s;
        getline(cin, s);

        for(auto it = s.cbegin(); it != s.cend(); ++it){
            if(*it == 's' || *it == 'S') sCount++;
            else if(*it == 't' || *it == 'T') tCount++;
        }
    }
    if(sCount < tCount) cout << "English";
    else cout << "French";
}