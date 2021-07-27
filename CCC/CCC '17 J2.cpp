#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    int b;
    scanf("%d", &a);
    scanf("%d", &b);

    long temp = a;
    for (int i = 1; i < b+1; i++) {
        temp += a * pow(10, i);
    }
    cout << temp;
}