#include <bits/stdc++.h>

using namespace std;

#define ll long long
const ll MOD = 1e9 + 7;

void multiply(ll mat[4], ll temp[4]){
    ll prod[4];
    prod[0] = ((mat[0]*temp[0])%MOD + (mat[1]*temp[2])%MOD)%MOD;
    prod[1] = ((mat[0]*temp[1])%MOD + (mat[1]*temp[3])%MOD)%MOD;
    prod[2] = ((mat[2]*temp[0])%MOD + (mat[3]*temp[2])%MOD)%MOD;
    prod[3] = ((mat[2]*temp[1])%MOD + (mat[3]*temp[3])%MOD)%MOD;
    copy(prod, prod + 4, mat);
}

int main(){
    ll mat[4] = {1,1,1,0};
    ll temp[4] = {1,1,1,0};

    unsigned long long n;
    cin >> n;
    n--;

    while(n > 0){
        if(n & 1){
            multiply(mat, temp);
        }
        multiply(temp, temp);
        n >>= 1;
    }
    cout << mat[1];
}