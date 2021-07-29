#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        stack<int> top;
        stack<int> branch;
        int cnt = 1;
        int N, temp;
        scanf("%d", &N);

        for(int j = 0; j < N; j++){
            scanf("%d", &temp);
            top.push(temp);
        }

        while(!(top.empty())){
            if(top.top() == cnt){
                top.pop();
                cnt++;
            }
            else if(!(branch.empty()) && branch.top() == cnt){ 
                branch.pop(); 
                cnt++;
            }
            else{
                branch.push(top.top());
                top.pop();
            }
        }

        while(!(branch.empty()) && branch.top() == cnt){
            branch.pop();
            cnt++;
        }

        if(cnt-1 == N) cout << "Y" << endl;
        else cout << "N" << endl;
    }
}