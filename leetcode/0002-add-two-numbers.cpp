/**
 * Definition for singly-linked list.
 */
#include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* result = head;
        int sum = 0;

        int carry = 0;

        while (l1 != NULL || l2 != NULL || carry) {
            sum = 0;

            if (l1 == NULL && l2 == NULL) {
                result->next = new ListNode(carry);
                break;
            }

            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }

            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            sum += carry;

            result->next = new ListNode(sum % 10);
            result = result->next;

            carry = sum / 10;
        }

        return head->next;
    }
};

int main() {
    ListNode* a_3 = new ListNode(3);
    ListNode* a_2 = new ListNode(4, a_3);
    ListNode* a_1 = new ListNode(2, a_2);

    ListNode* b_3 = new ListNode(4);
    ListNode* b_2 = new ListNode(6, b_3);
    ListNode* b_1 = new ListNode(5, b_2);

    Solution s;
    ListNode* final = s.addTwoNumbers(a_1, b_1);
    ListNode* tmpPtr = final;
    while (tmpPtr != NULL) {
        cout << tmpPtr->val << "\n";
        tmpPtr = tmpPtr->next;
    }
    return 0;
}