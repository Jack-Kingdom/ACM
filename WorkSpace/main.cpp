#include <iostream>
#include <random>

using namespace std;

template<typename T>
void merge_sort(T lst[], int length) {
    /*
     * 功能：对序列 lst 进行归并排序，自顶向下，递归操作
     * 参数：lst：序列指针；length：序列长度
     * 返回值：无
     */

    // 申请临时空间
    T *tmp = new T[length];

    auto merge = [&lst, &tmp](int first, int first_tail, int second, int second_tail) {

        // 存在任一子串的长度大于 2 ，则将其拆分成两个子串归并
        int mid = 0;
        if (first_tail - first > 2) {
            mid = (first_tail - first) / 2;
            merge(first, mid, mid, first_tail);
        }
        if (second_tail - second > 2) {
            mid = (second_tail - second) / 2;
            merge(second, mid, mid, second);
        }

        // 临时空间的索引
        int i = 0;

        // 归并操作,两个序列均未取完，则先取小的
        while (first < first_tail && second < second_tail) {
            tmp[i++] = lst[first] < lst[second] ? lst[first++] : lst[second++];
        }

        // 存在一个序列已经取完，则将另一序列剩下的元素取尽
        while (first < first_tail) tmp[i++] = lst[first++];
        while (second < second_tail) tmp[i++] = lst[second++];

        // 回填
        while (i--) lst[--second_tail] = tmp[i];

    };

    // 调用
    merge(0, length, length, length);

    // 删除申请的空间
    delete[] tmp;
}


int main() {
    int length = 100;
    int *lst = new int[length];
    for (int i = 0; i < length; i++) {
        lst[i] = rand() % length + 1;
    }

    merge_sort(lst, length);
    for (int i = 0; i < length; i++) {
        cout << lst[i] << " ";
    }

    return 0;
}