#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    float b, bmi;
    scanf("%d", &a);
    scanf("%f", &b);
    
    bmi = a/(b*b);
    
    if(bmi > 25) cout << "Overweight";
    else if(bmi < 18.5) cout << "Underweight";
    else cout << "Normal weight";
}