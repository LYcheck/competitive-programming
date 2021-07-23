#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int adjust(int timeTo, int adjust){
    int a, b, c, d, nnew, carry;
    
    a = timeTo % 100;
    b = adjust % 100;
    c = (timeTo-a) / 100;
    d = (adjust-b) / 100;
    
    carry = (a+b)/60;
    nnew = ((c+d+carry)%24)*100 + ((a+b)%60);
    return nnew;
}

int main() {
    int a;
    scanf("%d", &a);
    
    cout << a << " in Ottawa" << endl;
    cout << adjust(a, 2100) << " in Victoria" << endl;
    cout << adjust(a, 2200) << " in Edmonton" << endl;
    cout << adjust(a, 2300) << " in Winnipeg" << endl;
    cout << a << " in Toronto" << endl;
    cout << adjust(a, 100) << " in Halifax" << endl;
    cout << adjust(a, 130) << " in St. John's";
}