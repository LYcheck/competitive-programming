#include <bits/stdc++.h>
using namespace std;

int main() {
    float asum, bsum;
    int d, e, w;
    cin >> d;
    cin >> e;
    cin >> w;

    asum = (d < 100) ? 0 : (d-100)*0.25;
    bsum = (d < 250) ? 0 : (d-250)*0.45;

    asum += (w*0.20 + e*0.15);
    bsum += (w*0.25 + e*0.35);

    cout << "Plan A costs " << asum << endl;
    cout << "Plan B costs " << bsum << endl;

    if(asum > bsum) cout << "Plan B is cheapest.";
    else if(asum < bsum) cout << "Plan A is cheapest.";
    else cout << "Plan A and B are the same price.";

}