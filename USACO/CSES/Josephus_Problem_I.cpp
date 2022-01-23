// #include <bits/stdc++.h>
#include <iostream>
#include <queue>
using namespace std;

#define ll long long

int main(){
    queue<int> q;
    ll n, a;
    cin >> n;
    for(int i = 1; i <= n; i++) q.push(i);

    bool flag = 0;
    while(q.size() != 0){
        flag ^= 1;
        if(!flag){
            cout << q.front() << " ";
            q.pop();
        }
        else{
            ll bruh = q.front();
            q.push(bruh);
            q.pop();
        }
    }
}