/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int c = 0;
        ListNode *a = head;
        ListNode *t = head;

        while(t != nullptr){
            t = t->next;
            c++;
        }

        c/=2;

        for(int i = 0; i < c; i++) a = a->next;

        return a;
    }
};