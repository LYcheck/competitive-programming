#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, nmin, nmax;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    
    nmin = min(a,b);
    if(c < nmin) nmin = c;
    nmax = max(a,b);
    if(c > nmax) nmax = c;
    
    cout << (a^b^c^nmin^nmax);
}