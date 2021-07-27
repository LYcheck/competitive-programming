#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    unordered_set<char> c ({'I', 'O', 'S', 'H', 'Z', 'X', 'N'});

    for (auto it = s.cbegin() ; it != s.cend(); ++it) {
        if(!(c.count(*it))){
            cout <<"NO";
            return 0;
        }
    }
    cout << "YES";
}