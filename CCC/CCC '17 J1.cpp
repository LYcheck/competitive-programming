#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);

    if(a > 0){
        if(b > 0) cout << "1";
        else cout << "4";
    }
    else{
        if(b > 0) cout << "2";
        else cout << "3";
    }
}