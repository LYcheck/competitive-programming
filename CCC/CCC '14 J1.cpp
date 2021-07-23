#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    
    if(a + b + c != 180) cout << "Error";
    else if(a == 60 && b == 60) cout << "Equilateral";
    else if(a == b || b == c || a == c) cout << "Isosceles";
    else cout << "Scalene";
}