#include <bits/stdc++.h>
using namespace std;

#define ll long long

const ll MOD = 1e9 + 7;

ll grid[1005][1005];
ll dp[1005][1005];
int main() {
    memset(dp, 0, sizeof(dp));
    ll h, w;
    cin >> h >> w;
    
    dp[0][0] = 1;
    
    for(int i = 0; i < h; i++){
        for(int j = 0; j < w; j++){
            char a;
            cin >> a;
            grid[i][j] = (a == '.') ? 1 : 0;
        }
    }

    for(int i = 1; i < w; i++){
      if(grid[0][i] == 0) break;
      dp[0][i] = 1;
    }

    for(int i = 1; i < h; i++){
      if(grid[i][0] == 0) break;
      dp[i][0] = 1;
    }

    for(int i = 1; i < h; i++){
        for(int j = 1; j < w; j++){
          if(grid[i][j] == 0 || (grid[i-1][j] == 0 && grid[i][j-1] == 0)) continue;

          if(grid[i-1][j] == 0) dp[i][j] = dp[i][j-1]%MOD;
          else if(grid[i][j-1] == 0) dp[i][j] = dp[i-1][j]%MOD;
          else dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD;
        }
    }

    cout << dp[h-1][w-1];
}