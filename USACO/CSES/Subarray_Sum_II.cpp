#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

ll nums[200005];
int main(){
    ll n, k;
    cin >> n >> k;
    nums[0] = 0;
    for(int i = 0; i < n; i++) cin >> nums[i+1];
    for(int i = 1; i < n+1; i++) nums[i] += nums[i-1];

    map<ll, ll> seen;
    ll res = 0;

    for(ll i = 0; i < n+1; i++){
        ll target = nums[i]-k;
        if(seen.count(target)) res += seen[target];

        if(seen.count(nums[i])) seen[nums[i]] += 1;
        else seen[nums[i]] = 1;
    }
    cout << res << endl;
    return 0;
}