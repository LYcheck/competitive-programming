#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

void setIO(string s) {
    freopen((s+".in").c_str(),"r",stdin);
    freopen((s+".out").c_str(),"w",stdout);
}

int harr[100005];
int parr[100005];
int sarr[100005];
int main(){
    setIO("hps");
    int n;
    cin >> n;

    for(int i = 1; i < n+1; i++){
        char a;
        cin >> a;
        switch(a){
            case 'H': harr[i] = 1; break;
            case 'P': parr[i] = 1; break;
            case 'S': sarr[i] = 1; break;
        }
    }
    
    for(int i = 1; i < n+1; i++){
        harr[i] += harr[i-1];
        parr[i] += parr[i-1];
        sarr[i] += sarr[i-1];
    }
    if(harr[n] == n or parr[n] == n or sarr[n] == n){
        cout << n; 
        return 0;
    }
    
    int maxsofar = 0;
    for(int k = 1; k < n+1; k++){
        int hpost, ppost, spost, premax, postmax;
        hpost = harr[n] - harr[k-1];
        ppost = parr[n] - parr[k-1];
        spost = sarr[n] - sarr[k-1];

        premax = max(harr[k], max(parr[k], sarr[k]));
        postmax = max(hpost, max(ppost, spost));
        maxsofar = max(maxsofar, postmax+premax);
    }
    cout << maxsofar;
}