class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        /*
         * 功能：将两个链表相加
         * 参数：l1,l2：两个链表的首指针
         * 返回值：链表的首指针
         */

        auto Head = new ListNode(0);    // new 一个节点用于保存首节点信息
        auto node = Head;

        int step = 0;   // 保存进位
        while (l1 || l2 || step) {  //  循环直至两链表到底且此时无进位
            node->next = new ListNode(0);   // 仅需运算，生成新的节点
            node = node->next;

            if (l1) node->val += l1->val;   //  节点存在就加上他的值
            if (l2) node->val += l2->val;

            node->val += step;   // 加上之前的进位
            step = node->val / 10; // 计算新的进位

            node->val %= 10;    //  只保留十进制下的值

            if (l1) l1 = l1->next;  // 若节点存在，则后移一位
            if (l2) l2 = l2->next;
        }

        node = Head->next;
        delete (Head);  //  Head 本身并不存数据，用完后销毁

        return node;
    }
};