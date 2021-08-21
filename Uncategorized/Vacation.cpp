#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll choices[100050][3];
ll dp[100050][3];

int main() {
    memset(dp, 0, sizeof(dp));
    int N;
    cin >> N;

    for(int a = 0; a < N; a++) cin >> choices[a][0] >> choices[a][1] >> choices[a][2];

    dp[0][0] = choices[0][0];
    dp[0][1] = choices[0][1];
    dp[0][2] = choices[0][2];
    

    for(int i = 1; i <= N; i++){
        dp[i][0] = choices[i][0] + max(dp[i-1][1], dp[i-1][2]);
        dp[i][1] = choices[i][1] + max(dp[i-1][0], dp[i-1][2]);
        dp[i][2] = choices[i][2] + max(dp[i-1][0], dp[i-1][1]);
    }
    ll a = max(dp[N-1][0], dp[N-1][1]);
    cout << max(a, dp[N-1][2]);
}