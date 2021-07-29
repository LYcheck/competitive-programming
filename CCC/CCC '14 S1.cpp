#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[105];
int main() {
    for(int q = 0; q < 105; q++) arr[q] = 1;
    int n, z, rem;
    scanf("%d", &n);

    for(int i = 1; i < n; i++) arr[i] = arr[i-1]+1;

    scanf("%d", &z);

    for(int j = 0; j < z; j++){
        int cnt = 0;
        scanf("%d", &rem);

        for(int k = 0; k < n; k++){
            if(arr[k] != -1) cnt++;

            if(cnt != 0 && cnt%rem == 0){
                arr[k] = -1;
                cnt = 0;
            } 
        }
    }

    for(int a = 0; a < n; a++) if(arr[a] != -1) cout << arr[a] << endl;
}