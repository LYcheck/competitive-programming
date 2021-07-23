#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    bool vlad = 0;
    bool graeme = 0;
    bool troy = 0;
    
    if(a > 2 && b < 5) troy = true;
    if(a < 7 && b > 1) vlad = true;
    if(a < 3 && b < 4) graeme = true;
    
    if(troy) cout << "TroyMartian" << endl;
    if(vlad) cout << "VladSaturnian" << endl;
    if(graeme) cout << "GraemeMercurian";
}