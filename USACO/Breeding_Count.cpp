#include <bits/stdc++.h>
using namespace std;

#define ll long long

void setIO(string s) {
    freopen((s+".in").c_str(),"r",stdin);
    freopen((s+".out").c_str(),"w",stdout);
}

ll arr1[100005];
ll arr2[100005];
ll arr3[100005];
int main(){
    setIO("bcount");
    ll n, q;
    cin >> n >> q;
    for(int i = 1; i < n+1; i++){
        ll a;
        cin >> a;
        switch(a){
            case 1: arr1[i] = a; break;
            case 2: arr2[i] = a; break;
            case 3: arr3[i] = a; break;
        }
    }

    for(int i = 1; i < n+1; i++){
        arr1[i] += arr1[i-1];
        arr2[i] += arr2[i-1];
        arr3[i] += arr3[i-1];
    }

    for(int j = 0; j < q; j++){
        ll low, up;
        cin >> low >> up;
        cout << (arr1[up]-arr1[low-1]) << " ";
        cout << (arr2[up]-arr2[low-1])/2 << " ";
        cout << (arr3[up]-arr3[low-1])/3 << endl;
    }

}