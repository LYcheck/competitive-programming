#include <bits/stdc++.h>

using namespace std;

#define ll long long

ll arr[1000050];
int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) cin >> arr[i];

    sort(arr, arr+n);

    ll left = 0;
    ll indL, indR;
    ll right = n-1;
    ll min = LLONG_MAX;

    while(left < right){
        ll temp = arr[left] + arr[right];
        if(abs(temp) < min){
            indL = left;
            indR = right;
            min = temp;
        }
        if(temp < 0) left++;
        else right--;
    }
    cout << min << "\n";
    cout << indL+1 << " " << indR+1;
}