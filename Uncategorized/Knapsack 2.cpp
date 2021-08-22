#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll weights[105];
ll vals[105];
ll dp[1000000050];
int main() {
    memset(dp, 0, sizeof(dp));
    unsigned long long N, W;
    cin >> N >> W;

    for(unsigned long long a = 0; a <= N; a++) cin >> weights[a] >> vals[a];

    for(unsigned long long i = 1; i <= N; i++){
        for(unsigned long long j = W; j >= 0; j--){
            if(weights[i-1] <= j) dp[j] = max(dp[j], dp[j-weights[i-1]] + vals[i-1]);
        }
    }
    cout << dp[W];
}