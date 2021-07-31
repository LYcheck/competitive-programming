#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int coins[100];
int dp[10005];
int main(){
    int total, n;
    scanf("%d", &total);
    scanf("%d", &n);

    for(int i = 0; i < n; i++) scanf("%d", &coins[i]);
    for(int j = 0; j < total+1; j++) dp[j] = 99999999;
    dp[0] = 0;

    for(int k = 1; k < total+1; k++){
        for(int a = 0; a < n; a++){
            if(k-coins[a] >= 0){
                dp[k] = min(dp[k], dp[k-coins[a]]+1);
            }
        }
    }
    cout << dp[total];
}