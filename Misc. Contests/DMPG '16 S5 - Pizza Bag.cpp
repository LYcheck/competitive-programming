#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll prefix[200010];
map<ll, ll> maxmap;
int main() {
    memset(prefix, 0, sizeof(prefix));
    int N, K;

    cin >> N >> K;

    for(int a = 0; a < N; a++){
        cin >> prefix[a];
        prefix[a+N] = prefix[a];
    }
    for(int b = 1; b < N+K; b++) prefix[b] += prefix[b-1];

    deque<ll> dq;
    ll left, right;
    left = right = 0;

    while(right < 2*N){
        while(dq.size() > 0 && prefix[dq[dq.size()-1]] > prefix[right]) dq.pop_back();
        dq.push_back(right);
        if(right+1 >= K){
            maxmap[left] = dq[0];
            left++;
        }
        right++;

        if(left > dq[0]) dq.pop_front();
    }

    ll maxsofar = 0;

    for(int b = 1; b < 2*N; b++) maxsofar = max(prefix[b] - maxmap[b], maxsofar);
    cout << maxsofar;
}