#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int clubs[35];
int dp[5285];
int main() {
    memset(clubs, 0, sizeof(clubs));
    int dist, n;
    
    scanf("%d", &dist);
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) scanf("%d", &clubs[i]);
    for(int bruh = 0; bruh < dist+1; bruh++) dp[bruh] = pow(2,30);
    dp[0] = 0;
    
    for(int j = 1; j < dist+1; j++){

        for(int k = 0; k < n; k++){
            
            if((j-clubs[k] >= 0) && (dp[j-clubs[k]]+1 < dp[j])){
                dp[j] = dp[j-clubs[k]]+1;
            }
        }
    }
    if(dp[dist] != pow(2,30)) cout << "Roberta wins in " << dp[dist] << " strokes.";
    else cout << "Roberta acknowledges defeat.";
}