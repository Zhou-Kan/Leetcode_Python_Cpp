#include <iostream>

class ListNode {
    public:
        int val;
        ListNode* next;
        ListNode(int val, ListNode* next) : val(val), next(next) {}
        ListNode(int val) : val(val), next(nullptr) {}
};

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* dummy = new ListNode(-1);
    ListNode* cur = dummy;
    while (list1 && list2) {
        if (list1->val > list2->val) {
            cur->next = new ListNode(list2->val);
            list2 = list2->next;
        } else {
            cur->next = new ListNode(list1->val);
            list1 = list1->next;
        }
        cur = cur->next;
    }
    if (list1) cur->next = list1;
    if (list2) cur->next = list2;
    return dummy->next;
}


int main() {
    return 0;
}
