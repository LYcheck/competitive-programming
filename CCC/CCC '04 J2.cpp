#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a;
    cin >> b;
    
    for(int i = 0; i <= (b-a); i+= 60){
        cout << "All positions change in year " << (a+i) << endl;
    }

}