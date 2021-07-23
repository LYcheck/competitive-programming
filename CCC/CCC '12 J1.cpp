#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    if(a >= b) cout << "Congratulations, you are within the speed limit!";
    else {
        cout << "You are speeding and your fine is $";
        if((b-a) > 30) cout << "500.";
        else if((b-a) < 21) cout << "100.";
        else cout << "270.";
    }
}