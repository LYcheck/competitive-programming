#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        if(s == "Scissors") cout << "Rock\n";
        else if(s == "Paper") cout << "Scissors\n";
        else if(s == "Rock") cout << "Paper\n";
        else if(s == "Fox") cout << "Foxen\n";
        else break;
    }
    return 0;
}