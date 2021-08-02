#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int c[105];
int main() {
    int mtime, n;
    cin >> mtime;
    cin >> n;

    for(int i = 0; i < n; i++) cin >> c[i];
    sort(c, c+n);

    int chtime, cnt;
    chtime = cnt = 0;

    for(int i = 0; i < n; i++){
      if(chtime < mtime){
        chtime += c[i];
        cnt++;
      }
      else break;
    }
    if(chtime > mtime) cout << cnt-1;
    else cout << cnt;
}