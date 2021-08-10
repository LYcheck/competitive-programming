#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll arr[105][105];
int main() {
    memset(arr, 0, sizeof(arr));
    int n;
    cin >> n;

    for(int i = 0; i <= n; i++){
        for(int j = 0; j < i; j++){
            cin >> arr[i][j];
        }
    }

    for(int i = n-1; i > -1; i--){
        if(i == 0) cout << arr[0][0] + max(arr[1][0], arr[1][1]);
        else{
            for(int j = 0; j <= i; j++){
                arr[i][j] += max(arr[i+1][j], arr[i+1][j+1]);
            }
        }
    }
}