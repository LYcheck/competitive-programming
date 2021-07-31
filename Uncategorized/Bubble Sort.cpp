#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int toSort[21];

void print(int arr[], int n){
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}
int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) cin >> toSort[i];
    print(toSort, n);
    
    for(int j = 0; j < n-1; j++){
        for(int k = 0; k < n-1-j; k++){
            if(toSort[k+1] < toSort[k]){
                swap(toSort[k+1], toSort[k]);
                print(toSort, n);
            }
        }
    }
}

    