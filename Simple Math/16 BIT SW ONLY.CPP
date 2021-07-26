#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    long long a, b, p;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        cin >> a >> b >> p;
        if(a*b != p) cout << "16 BIT S/W ONLY\n";
        else cout << "POSSIBLE DOUBLE SIGMA\n";
    }
}