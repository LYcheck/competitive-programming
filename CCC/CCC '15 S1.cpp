#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    stack<int> nums;
    int n, cur;
    int sum = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> cur;
        if(cur == 0 && !(nums.empty())){
            sum -= (int)nums.top();
            nums.pop();
        } 
        else{ 
            nums.push(cur);
            sum += cur;
        }
    }
    cout << sum;
}