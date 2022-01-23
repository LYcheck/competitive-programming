#include <bits/stdc++.h>

using namespace std;

#define ll long long

void setIO(string s) {
    freopen((s+".in").c_str(),"r",stdin);
    freopen((s+".out").c_str(),"w",stdout);
}

ll arr[50005];
int mod[7];
int main(){
    setIO("div7");
    memset(mod, -1, sizeof(mod));
    ll n;
    cin >> n;
    
    for(int i = 1; i < n+1; i++) {
        ll a;
        cin >> a;
        arr[i] = a%7;
    }

    for(int j = 1; j < n+1; j++){
        arr[j] = (arr[j] + arr[j-1])%7;
    }

    int maxsofar = 0;
    for(int k = 0; k < n+1; k++){
        if(mod[arr[k]] == -1) mod[arr[k]] = k;
        if(arr[k]%7 == 0) maxsofar = max(maxsofar, k);
        else if(mod[arr[k]%7] != -1) maxsofar = max(maxsofar, k-mod[arr[k]]);
        
        //cout << "prefix num = " << arr[k] << " modnum = " << mod[arr[k]] << " test: " << k-mod[arr[k]] << endl;
    }

    cout << maxsofar;
}