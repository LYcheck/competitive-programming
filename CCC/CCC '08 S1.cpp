#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    string temp, cur;
    int itemp, icur;
    
    icur = 205;
    
    cin >> temp >> itemp;
    while(temp != "Waterloo"){
        if(itemp < icur){
            icur = itemp;
            cur = temp;
        } 
        
        cin >> temp >> itemp;
    }
    cout << cur;
}