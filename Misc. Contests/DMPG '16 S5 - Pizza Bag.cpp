#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll prefix[200010];
map<ll, ll> maxmap;
int main() {
    memset(prefix, 0, sizeof(prefix));
    ll N, K;
    cin >> N >> K;

    for(ll a = 1; a < N+1; a++){
        cin >> prefix[a];
        prefix[a+N] = prefix[a];
    }

    for(ll b = 1; b < N+K+1; b++) prefix[b] += prefix[b-1];

    deque<ll> dq;
    dq.push_back(0);
    ll res = -1;
    
    for(ll i = 1; i < N+K+1; i++){
        while(!dq.empty() && (i-dq.front()) > K) dq.pop_front();
        if(i >= K) res = max(res, prefix[i] - prefix[dq.front()]);
        while(!dq.empty() && prefix[dq.back()] > prefix[i]) dq.pop_back();
        dq.push_back(i);
    }

    cout << res;
}