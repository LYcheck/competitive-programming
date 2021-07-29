#include <bits/stdc++.h>
using namespace std;

int dm[105];
int pe[105];
int main() {
    int choice, n;
    cin >> choice;
    cin >> n;

    for(int i = 0; i < n; i++) cin >> dm[i];
    for(int j = 0; j < n; j++) cin >> pe[j];

    int sum = 0;

    if(choice == 1){
        sort(dm, dm+n);
        sort(pe, pe+n);
    }
    else{
        sort(dm, dm+n);
        sort(pe, pe+n, greater<int>());
    }
    
    for(int k = 0; k < n; k++) sum += max(dm[k], pe[k]);

    cout << sum;

}