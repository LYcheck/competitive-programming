#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[5] = {0};
int main() {
    for(int i = 0; i < 4; i++) scanf("%d", &arr[i+1]);
    for(int a = 1; a < 5; a++) arr[a] = arr[a] + arr[a-1];
    
    for(int j = 0; j < 5; j++){
        for(int k = 0; k < 5; k++){
            if(k < 4) cout << abs(arr[j] - arr[k]) << " ";
            else cout << abs(arr[j] - arr[k]);
        }
        if(j < 4) cout << endl;
    }
}