#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[101];
int main() {
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++) scanf("%d", &arr[i]);
    
    sort(arr, arr+N);
    
    for(int i = 0; i < N; i++) cout << arr[i] << endl;
}