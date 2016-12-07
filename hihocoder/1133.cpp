//
// Created by Jack King on 12/7/16.
//

#include <iostream>

using namespace std;

template<typename T>
int unsorted_index_binary_search(T *lst, int length, int index) {
    /*
     * 功能：在无序数组 lst 中查找第 index 小的数
     * 参数：lst 待查找的数组、length 数组的长度、index 排序后该元素的下标，也反映了第 index 小的数
     * 返回值：如果找到，返回 lst[index]；否则返回 -1
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

        // 返回快排分割定序后的索引即可
        return i;
    };

    // 二分查找
    int head = 0, tail = length - 1;
    while (head <= tail) {

        // pivot_index 基准数的下标
        int pivot_index = quick_separate(head, tail);

        // 找到元素，返回对应的值
        if (pivot_index == index) return lst[index];

        if (pivot_index > index) tail = pivot_index - 1;
        else head = pivot_index + 1;
    }

    return -1;
}

int main() {
    int n, k;
    cin >> n >> k;

    int *lst = new int[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    cout << unsorted_index_binary_search(lst, n, k - 1);
    return 0;
}