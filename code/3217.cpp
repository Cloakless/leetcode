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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        set<int> num_set;
        for (int i = 0; i < nums.size(); i++) {
            num_set.insert(nums[i]);
        }
        // Find new head
        while (num_set.count(head->val) == 1) {
            head = head->next;
        }
        // Remove nodes
        ListNode *curr = head;
        while (curr != NULL) {
            while (curr->next != NULL && num_set.count(curr->next->val) == 1) {
                curr->next = curr->next->next;
            }
            curr = curr->next;
        }
        return head;
    }
};
