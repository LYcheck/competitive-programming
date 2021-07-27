#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

int main() {
    int a, b, cnt;
    scanf("%d", &a);
    scanf("%d", &b);
    
    cnt = 0;
    int uppercbrt = cbrt(b);
    int uppersqrt = sqrt(b);
    int lowercbrt = cbrt(a);
    int lowersqrt = sqrt(a);
    
    for(int i = lowersqrt; i <= uppersqrt; i++){
        for(int j = lowercbrt; j <= uppercbrt; j++){
            if(i*i == j*j*j) cnt++;
        }
    }
    cout << cnt;
}