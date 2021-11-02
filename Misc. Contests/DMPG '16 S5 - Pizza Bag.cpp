#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll prefix[100005];
int main() {
    memset(prefix, 0, sizeof(prefix));
    int N, K;

    cin >> N >> K;

    for(int a = 0; a < N; a++) cin >> prefix[a];
    for(int b = 1; b < N; b++) prefix[b] += prefix[b-1];

    
}