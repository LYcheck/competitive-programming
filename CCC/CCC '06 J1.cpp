#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    map<int, int> bu {{1, 461}, {2, 431}, {3, 420}, {4, 0}};
    map<int, int> si {{1, 100}, {2, 57}, {3, 70}, {4, 0}};
    map<int, int> dr {{1, 130}, {2, 160}, {3, 118}, {4, 0}};
    map<int, int> de {{1, 167}, {2, 266}, {3, 75}, {4, 0}};

    int a,b,c,d;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);

    cout << "Your total Calorie count is " << (bu[a] + si[b] + dr[c] + de[d]) << ".";
}