#include <bits/stdc++.h>

using namespace std;

#define arr array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;

int main() {
    int b, n;
    deque<string> d;
    d.push_back("A");
    d.push_back("B");
    d.push_back("C");
    d.push_back("D");
    d.push_back("E");
    
    while(b != 4){
        scanf("%d", &b);
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            switch(b){
                case 1:
                    d.push_back(d[0]);
                    d.pop_front();
                    break;
                case 2:
                    d.push_front(d[4]);
                    d.pop_back();
                    break;
                case 3:
                    swap(d[0], d[1]);
                    break;
                case 4:
                    cout << d[0] << " " << d[1] << " " << d[2] << " " << d[3] << " " << d[4];
                    break;
            }
        }
    }
    return 0;
}