#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool isDupe(int n){
    int a,b,c,d;
    a = n/1000;
    b = (n/100)%10;
    c = (n/10)%10;
    d = n%10;

    if(n > 999) return (!(a^b) || !(a^c) || !(a^d) || !(b^c) || !(b^d) || !(c^d));
    else if(n) return (!(b^c) || !(b^d) || !(c^d));
    else return (!(c^d));
}

int main() {
    int n;
    cin >> n;
    n++;
    
    if(n < 11){
        cout << n;
        return 0;
    }
    else if(n > 9876){
        cout << 10234;
        return 0;
    }
    
    while(isDupe(n)) n++;

    cout << n;
}