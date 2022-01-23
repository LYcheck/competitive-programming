#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll arr[200005];
int main(){
    ll n;
    cin >> n;

    for(int i = 0; i < n; i++) cin >> arr[i];
    
    vector< vector<ll> > piles;

    for(int j = 0; j < n; j++){
        ll num = arr[j];
        if(piles.size() == 0){
            vector<ll> temp; 
            temp.push_back(num);
            piles.push_back(temp);
            continue;
        }

        ll l, r;
        l = 0;
        r = piles.size()-1;
        
        while(l < r){
            ll m = (l+r)/2;
            if(num >= piles[m][piles[m].size()-1]) l = m+1;
            else r = m;
        }
        
        if(piles[l][piles[l].size()-1] <= num){
            vector<ll> temp; 
            temp.push_back(num);
            piles.push_back(temp);
        }
        else piles[l].push_back(num);
    }

    // for(int k = 0; k < piles.size(); k++){
    //     for(int l = 0; l < piles[k].size(); l++){
    //         cout << piles[k][l] << " ";
    //     }
    //     cout << endl;
    // }
    cout << piles.size();
}