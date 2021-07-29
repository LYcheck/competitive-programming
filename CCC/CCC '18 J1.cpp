#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    
    if(!(b==c)) cout << "answer";
    else if(!(a==8 || a==9)) cout << "answer";
    else if(!(d==8 || d==9)) cout << "answer";
    else cout << "ignore";

}