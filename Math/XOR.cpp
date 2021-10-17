#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

int modResult(int z){
    int n = z%4;
    
    if(n == 1) return 1;
    else if(n == 2) return z+1;
    else if(n == 3) return 0;
    else if(n == 0) return z;
    return 0;
}

int main() {
    int n, a, b, xor1, xor2;
    
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        
        xor1 = modResult(a-1);
        xor2 = modResult(b);
        
        cout << (xor1^xor2) << endl;
    }
}