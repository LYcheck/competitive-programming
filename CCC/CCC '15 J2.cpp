#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    int happy, sad;
    happy = sad = 0;
    
    for(int i = 0; i < s.length()-2; i++){
        if((s.at(i) == ':') && (s.at(i+1) == '-')){
            if(s.at(i+2) == ')') happy++;
            else if(s.at(i+2) == '(') sad++;
        }
    }

    if(happy == 0 && sad == 0) cout << "none";
    else if(happy == sad) cout << "unsure";
    else if(happy > sad) cout << "happy";
    else cout << "sad";
}