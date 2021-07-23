#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int arr[4] = {1,2,3,4};
int main() {
    string s;
    cin >> s;
    
    for (auto it = s.cbegin() ; it != s.cend(); ++it) {
        if(*it == 'H'){
            swap(arr[2], arr[0]);
            swap(arr[3], arr[1]);
        }
        else if(*it == 'V'){
            swap(arr[1], arr[0]);
            swap(arr[3], arr[2]);
        }
    }
    
    cout << arr[0] << " " << arr[1] << endl;
    cout << arr[2] << " " << arr[3];
}