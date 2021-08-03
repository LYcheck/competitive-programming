#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll heights[100005];
ll dp[100005];
int main() {
    memset(dp, 0, sizeof(dp));
    int N;
    cin >> N;

    for(int a = 0; a < N; a++) cin >> heights[a];
    
    dp[1] = abs(heights[0]-heights[1]);
    
    for(int i = 2; i < N; i++){
        dp[i] = min(dp[i-2] + abs(heights[i-2]-heights[i]), dp[i-1] + abs(heights[i-1]-heights[i]));
    }
    cout << dp[N-1];
}