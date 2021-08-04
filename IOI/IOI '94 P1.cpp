#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll temp[105];
ll fin[105];
int main() {
    memset(temp, 0, sizeof(temp));
    memset(fin, 0, sizeof(fin));
    int n;
    cin >> n;
    
    for(int i = 1; i <= n; i++){
        for(int j = 0; j < i; j++) cin >> temp[j];

        fin[0] += temp[0];

        fin[i] = temp[i-1];  

        
        for(int k = 1; k < i-1; k++){
            fin[k] += max(temp[k-1], temp[k]);
        }
    }

    int nmax = -1;
    for(int a = 0; a < n; a++) if(fin[a] > nmax) nmax = fin[a];

    cout << nmax;
}