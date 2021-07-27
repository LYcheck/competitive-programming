#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int w = 0;

    for(int i = 0; i < 6; i++){
        char c;
        cin >> c;
        if(c == 'W') w++;
    }
    if(w == 0) cout << -1;
    else if(w < 3) cout << 3;
    else if(w < 5) cout << 2;
    else cout << 1;
}