#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);

    if(a == 2){
        if(b < 18) cout << "Before";
        else if(b > 18) cout << "After";
        else cout << "Special";
    }
    else if(a > 2) cout << "After";
    else cout << "Before";
}