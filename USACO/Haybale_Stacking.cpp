#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

void setIO(string s) {
    freopen((s+".in").c_str(),"r",stdin);
    freopen((s+".out").c_str(),"w",stdout);
}

ll nums[100005];
int main(){
    setIO("stacking");
    memset(nums, 0, sizeof(nums));
    ll n, k;
    cin >> n >> k;
    for(int i = 0; i < k; i++){
        int a, b;
        cin >> a >> b;
        nums[a] += 1;
        nums[b+1] -= 1;
    }

    for(int i = 1; i < n+1; i++) nums[i] += nums[i-1];
    
    sort(nums+1, nums+n+1);
    for(int i = 1; i < n+1; i++) cout << nums[i] << " ";
    cout << nums[n/2+1];
    
    return 0;
}