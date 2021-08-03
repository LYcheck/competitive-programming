#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll weights[105];
ll vals[105];
ll dp[1000005];
int main() {
    memset(dp, 0, sizeof(dp));
    int N, W;
    cin >> N >> W;

    for(int a = 0; a <= N; a++) cin >> weights[a] >> vals[a];

    for(int i = 1; i <= N; i++){
        for(int j = W; j >= 0; j--){
            if(weights[i-1] <= j) dp[j] = max(dp[j], dp[j-weights[i-1]] + vals[i-1]);
        }
    }
    cout << dp[W];
}