#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    n = (n>5) ? (abs(10-n)) : n;
    if(n & 1) cout << (int)(0.5*n+0.5);
    else cout << (int)(0.5*(n+1)+0.5);
}