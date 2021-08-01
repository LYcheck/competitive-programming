#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

// ll dp[105][105];
// ll weights[105];
// ll vals[105];
// int main() {
//     int N, W;
//     cin >> N >> W;

//     for(int a = 0; a <= N; a++) cin >> weights[a] >> vals[a];

//     for(int i = 0; i <= N; i++){
//         for(int j = 0; j <= W; j++){
//             if(i == 0 || j == 0) dp[i][j] = 0;
//             else if(weights[i-1] <= j) dp[i][j] = max(vals[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j]);
//             else dp[i][j] = dp[i-1][j];
//         }
//     }
//     cout << dp[N][W];
// }

int weights[105];
int vals[105];
int dp[1000005];
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