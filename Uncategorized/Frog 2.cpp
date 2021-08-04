#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll heights[100005];
ll dp[100005];
int main() {
    int N, K;
    cin >> N >> K;

    for(int a = 0; a < N; a++) cin >> heights[a];
    for(int b = 0; b < N+1; b++) dp[b] = pow(2,30);
    
    dp[0] = 0;
    
    for(int i = 1; i < N; i++){
        for(int j = 1; j <= K; j++){
            if(i-j >= 0){
                dp[i] = min(dp[i], dp[i-j] + abs(heights[i-j]-heights[i]));
            }
        }
    }
    cout << dp[N-1];
}