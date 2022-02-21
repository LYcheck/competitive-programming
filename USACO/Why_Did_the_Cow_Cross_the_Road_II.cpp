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
    setIO("maxcross");
    nums[0] = 0;
    ll n, k, b;
    cin >> n >> k >> b;
    for(int i = 1; i < n+1; i++) nums[i] = 1;

    for(int j = 0; j < b; j++){
        int id;
        cin >> id;
        nums[id] = 0;
    }
  
    for(int i = 1; i < n+1; i++) nums[i] += nums[i-1];

    ll idx = k;
    ll bestsofar = 100000;
    while(idx < n+1){
        bestsofar = min(bestsofar, k-(nums[idx]-nums[idx-k]));
        idx++;
    }
    cout << bestsofar;
    return 0;
}