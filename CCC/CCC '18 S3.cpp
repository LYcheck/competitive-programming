#include <bits/stdc++.h>

using namespace std;

#define ll long long

void print(ll n, ll m, char grid[105][105]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

void print(ll n, ll m, ll grid[105][105]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

char grid[105][105];
ll ansGrid[105][105];
int main() {
    memset(grid, 0, sizeof(grid));
    ll n, m;
    pair<ll, ll> start;
    cin >> n >> m;
    
    map<pair<ll, ll>, bool> seen;
    map<char, bool> dirs;
    dirs['L'] = 0; dirs['R'] = 0; dirs['U'] = 0; dirs['D'] = 0;
    vector< pair<ll, ll> > cams;
    vector< pair<ll, ll> > spots;

    for(ll i = 0; i < n; i++){
        for(ll j = 0; j < m; j++){
            cin >> grid[i][j];
            if(grid[i][j] == 'C') cams.push_back(make_pair(i, j));
            if(grid[i][j] == '.') spots.push_back(make_pair(i, j));
            if(grid[i][j] == 'S') start = {i, j};
            ansGrid[i][j] = -1;
        }
    }

    // print(n, m, grid);

    for(ll k = 0; k < cams.size(); k++){
        ll x, y;
        x = cams[k].first;
        y = cams[k].second;

        for(ll t = x; t < n && grid[t][y] != 'W'; t++) if(!dirs.count(grid[t][y])) grid[t][y] = 'C';
        for(ll t = x; t >= 0 && grid[t][y] != 'W'; t--) if(!dirs.count(grid[t][y])) grid[t][y] = 'C';
        for(ll t = y; t < m && grid[x][t] != 'W'; t++) if(!dirs.count(grid[x][t])) grid[x][t] = 'C';
        for(ll t = y; t >= 0 && grid[x][t] != 'W'; t--) if(!dirs.count(grid[x][t])) grid[x][t] = 'C';
    }

    queue< pair< pair<ll, ll>, ll> > q;
    q.push(make_pair(start, 0));

    while(q.size() > 0){
        pair< pair<ll, ll>, ll > curr = q.front();
        q.pop();
        // cout << "PROCESSING " << curr.first.first << ", " << curr.first.second << endl;
        ll x, y, dist;
        x = curr.first.first; y = curr.first.second; dist = curr.second;
        if(grid[x][y] == 'W' || grid[x][y] == 'C' || seen.count(curr.first) || x < 0 || x >= n || y < 0 || y >= m) continue;
        else if(dirs.count(grid[x][y])){
            switch(grid[x][y]){
                case 'U':
                    q.push(make_pair(make_pair(x-1, y), dist));
                    break;
                case 'D':
                    q.push(make_pair(make_pair(x+1, y), dist));
                    break;
                case 'L':
                    q.push(make_pair(make_pair(x, y-1), dist));
                    break;
                case 'R':
                    q.push(make_pair(make_pair(x, y+1), dist));
                    break;

                seen[curr.first] = 1;
            }
        }
        else{
            ansGrid[x][y] = dist;
            q.push(make_pair(make_pair(x+1, y), dist+1));
            q.push(make_pair(make_pair(x-1, y), dist+1));
            q.push(make_pair(make_pair(x, y+1), dist+1));
            q.push(make_pair(make_pair(x, y-1), dist+1));
            seen[curr.first] = 1;
        }

    }
    
  for(ll k = 0; k < spots.size(); k++){
        ll x, y;
        x = spots[k].first;
        y = spots[k].second;
        cout << ansGrid[x][y] << endl;
  }

    // cout << endl;
    // print(n, m, grid);
    // cout << endl;
    // print(n, m, ansGrid);
}