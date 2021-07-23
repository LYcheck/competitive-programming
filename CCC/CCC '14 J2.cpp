#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b;
    a = 0;
    b = 0;

    scanf("%d", &n);
    
    string s;
    cin >> s;
    
    for (auto it = s.cbegin() ; it != s.cend(); ++it) {
        if(*it == 'A') a++;
        else if(*it == 'B') b++;
    }
    
    if(a > b) cout << "A";
    else if(b > a) cout << "B";
    else cout << "Tie";
}