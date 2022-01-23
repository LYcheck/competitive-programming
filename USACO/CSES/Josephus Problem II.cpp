#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    queue<ll> q;
    ll n, k;
    cin >> n >> k;
    for(ll i = 1; i <= n; i++) q.push(i);

    ll ctr = k+1;
    while(q.size() != 0){
        ctr -= 1;
        if(!ctr){
            cout << q.front() << " ";
            q.pop();
            ctr = (k+1) % n;
        }
        else{
            ll bruh = q.front();
            q.push(bruh);
            q.pop();
        }
    }
}
