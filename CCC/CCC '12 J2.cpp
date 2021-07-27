#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int fish[4];
int main() {
    for(int i = 0; i < 4; i++) scanf("%d", &fish[i]);
    bool rise, fall, constant;
    rise = fall = constant = true;

    for(int j = 1; j < 4; j++){
        rise = rise & (fish[j] > fish[j-1]);
        fall = fall & (fish[j] < fish[j-1]);
        constant = constant & (fish[j] == fish[j-1]);
    }

    if(rise) cout << "Fish Rising";
    else if(fall) cout << "Fish Diving";
    else if(constant) cout << "Fish At Constant Depth";
    else cout << "No Fish";
}