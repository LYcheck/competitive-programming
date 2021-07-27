#include <iostream>
#include <bits/stdc++.h>
using namespace std;

char ans[10010];
int main() {
    int n;
    scanf("%d", &n);
    int cnt = 0;
    for(int i = 0; i < (2*n); i++) cin >> ans[i];  
    for(int j = 0; j < n; j++) if(ans[j] == ans[j+n]) cnt++;

    cout << cnt;
}