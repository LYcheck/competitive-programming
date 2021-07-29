#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int pos = 1;
    int roll;

    while(true){
        scanf("%d", &roll);

        if(roll == 0) break;
        else if(pos+roll > 100){
            cout << "You are now on square " << pos << endl;
            continue;
        } 
        else pos += roll;

        if(pos == 54) pos = 19;
        else if(pos == 90) pos = 48;
        else if(pos == 99) pos = 77;
        else if(pos == 9) pos = 34;
        else if(pos == 40) pos = 64;
        else if(pos == 67) pos = 86;

        cout << "You are now on square " << pos << endl;

        if(pos == 100) break;
    }
    
    if(roll == 0){
        cout << "You Quit!";
        return 0;
    } 
    else{
        cout << "You Win!";
        return 0;
    } 
}