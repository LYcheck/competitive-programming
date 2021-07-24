#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, x1, y1, x2, y2;
    cin >> a >> b;
    cin >> x1 >> y1 >> x2 >> y2;
    
    bool horiz = false;
    bool vert = false;
    
    horiz = x1 < a && a < x2;
    vert = y1 < b && b < y2;
    
    if(horiz && vert) cout << "Yes";
    else cout << "No";
}