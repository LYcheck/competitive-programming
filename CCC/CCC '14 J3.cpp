#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b, ant, dav;
    cin >> n;
    
    ant = dav = 100;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        if(a > b) dav -= a;
        else if(b > a) ant -= b;
    }
    cout << ant << endl;
    cout << dav;
}