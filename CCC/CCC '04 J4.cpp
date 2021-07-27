#include <bits/stdc++.h>
using namespace std;

int main() {
    string key, s, ans;
    cin >> key;
    cin >> s;
    ans = "";
    
    int keyLen, sLen, keyLeft, sLeft, shift;
    keyLen = key.length();
    sLen = s.length();
    sLeft = 0;
    keyLeft = 0;

    while(sLeft < sLen){
        if(!(isalnum(s[sLeft]))){
            sLeft++;
            continue;
        }

        shift = ((int)s[sLeft] + ((int)key[keyLeft]-65) < 91) ? (int)s[sLeft] + ((int)key[keyLeft]-65) : (int)s[sLeft] + ((int)key[keyLeft]-65) - 26;
        ans += (char)shift;
        sLeft++;
        keyLeft++;
        keyLeft = keyLeft%keyLen;
    }
    cout << ans;
}