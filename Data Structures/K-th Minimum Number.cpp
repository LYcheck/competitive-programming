#include <bits/stdc++.h>

using namespace std;

#define ll long long
const int MAX_N = 1e5 + 1;

// ll nums[200005];
// int main(){
//     ll n, q;

//     cin >> n >> q;

//     for(int i = 0; i < n; i++) cin >> nums[i];

//     ll lastAns = 0;
//     for(int j = 0; j < q; j++){
//         priority_queue <ll, vector<ll>, greater<ll>> minheap;
//         ll left, right, k;
//         cin >> left >> right >> k;

//         left ^= lastAns;
//         right ^= lastAns;
//         k ^= lastAns;

//         for(int a = left-1; a < right; a++) minheap.push(nums[a]);
//         for(int b = 0; b < k-1; b++) minheap.pop();

//         lastAns = minheap.top();
//         cout << lastAns << "\n";
//     }

// Segment tree learning [UNORIGINAL]

struct Vertex{
    Vertex *left, *right;
    int sum;

    Vertex(int val) : left(nullptr), right(nullptr), sum(val) {};
    Vertex(Vertex *left, Vertex *right) : left(left), right(right), sum(0) {
        if(left) sum += left->sum;
        if(right) sum += right->sum;
    }
};

Vertex* build(ll treeLeft, ll treeRight){
    if(treeLeft == treeRight) return new Vertex(0);
    ll treeMid = (treeLeft + treeRight) / 2;
    return new Vertex(build(treeLeft, treeMid), build(treeMid+1, treeRight));

}

Vertex* update(Vertex* vert, ll treeLeft, ll treeRight, ll pos){
    if(treeLeft == treeRight) return new Vertex(vert->sum+1);
    ll treeMid = (treeLeft + treeRight) / 2;
    if(pos <= treeMid) return new Vertex(update(vert->left, treeLeft, treeMid, pos), vert->right);
    else return new Vertex(vert->left, update(vert->right, treeMid+1, treeRight, pos));
}

ll extract(Vertex* vertLeft, Vertex* vertRight, ll treeLeft, ll treeRight, ll k){
    if(treeLeft == treeRight) return treeLeft;
    ll treeMid = (treeLeft + treeRight) / 2;
    ll leftCnt = vertRight->left->sum - vertLeft->left->sum;
    if(leftCnt >= k) return extract(vertLeft->left, vertRight->left, treeLeft, treeMid, k);
    return extract(vertLeft->right, vertRight->right, treeMid+1, treeRight, k-leftCnt);
}

ll nums[200005];
int main(){
    vector<Vertex*> roots;
    ll n, q;

    cin >> n >> q;

    for(int i = 0; i < n; i++) cin >> nums[i];

    ll treeLeft = 0;
    ll treeRight = MAX_N;
    ll lastAns = 0;

    roots.push_back(build(treeLeft, treeRight));

    for(int i = 0; i < n; i++){
        roots.push_back(update(roots.back(), treeLeft, treeRight, nums[i]));
    }

    roots.push_back(build(treeLeft, treeRight));

    for(int j = 0; j < q; j++){
        ll left, right, k;
        treeLeft = 0;
        treeRight = MAX_N;

        cin >> left >> right >> k;

        left ^= lastAns;
        right ^= lastAns;         
        k ^= lastAns;

        lastAns = extract(roots[left-1], roots[right-1], treeLeft, treeRight, k);
        cout << lastAns << "\n";
    }
}