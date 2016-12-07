#include <iostream>

using namespace std;

template<typename T>
int unsorted_binary_search(T lst[], int length, T aim) {
    /*
     * 功能：非有序数组的二分查找
     * 参数：lst 待查找的数组，length 数组的长度，aim 待查找的元素
     * 返回值：若找到，目标元素的下标（排序后），否则返回 -1
     */

    // 采用快排的思想对序列进行一次分割
    auto quick_separate = [&lst](int head, int tail) {
        // 选择基准
        T pivot = lst[head];

        int i = head, j = tail;
        while (i < j) {
            while (i < j and lst[j] > pivot) j--;
            lst[i] = lst[j];
            while (i < j and lst[i] < pivot) i++;
            lst[j] = lst[i];
        }

        // 回填
        lst[i] = pivot;
        return make_pair(pivot, i);
    };

    // 二分查找
    int head = 0, tail = length - 1;
    while (head <= tail) {
        auto tmp = quick_separate(head, tail);
        auto pivot = tmp.first;
        auto index = tmp.second;

        if (pivot == aim) return index;
        else if (pivot < aim) head = index + 1;
        else tail = index - 1;
    }

    // 查找失败，返回 -1
    return -1;
}

int main() {
    int n, k;
    cin >> n >> k;

    int *lst = new int[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    int result = unsorted_binary_search(lst, n, k);
    if (result != -1) cout << result + 1 << endl;
    else cout << -1 << endl;

    return 0;
}