#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[1005];
int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) scanf("%d", &arr[i]);
    
    sort(arr, arr+n);
    
    for(int i = 0; i < n; i++) cout << arr[i] << endl;
}