// 线性表的顺序表示
// Created by Jack King on 9/2/16.
// please compile code with c++11
#include <cstdlib>
#include <cassert>
#include <type_traits>

#define LIST_INIT_SIZE 100  //线性表存储空间的初始分配量
#define LIST_INCREMENT 10    //线性表存储空间的分配增量

template<typename ElemType>
struct ArrayList {
    ElemType *elem; // 存储空间基址, start with 0
    int length; // 当前线性表的长度, start with 1
    int list_size;  // 当前分配的存储容量(以sizeof(ElemType)为单位), start with 1

    ArrayList() {
        // 构造一个空的线性表
        this->elem = (ElemType *) malloc(LIST_INIT_SIZE * sizeof(ElemType));
        assert(this->elem != nullptr);
        this->length = 0; //空表长度为0
        this->list_size = LIST_INIT_SIZE; //初始存储容量
    }

    ~ArrayList() {
        free(this->elem);
    }

    void expand(int size = LIST_INCREMENT) {
        realloc(this->elem, (size_t) this->list_size + size);   // 对空间长度扩容
        assert(this->elem != nullptr);
        this->list_size += size;  // update List length

    }


    void insert(ElemType ele, int pos) {
        // pos start with 0, insert in front of pos
        assert(pos >= 0 || pos <= this->length);
        if (this->length == this->list_size)
            this->expand(); // expand default size if list_size limited
        for (int i = this->length - 1; i >= pos; i--) {
            this->elem[i + 1] = this->elem[i];
        }
        this->elem[pos] = ele;
        this->length += 1;

    }

    void erase(int pos) {
        // erase element at pos. pos start with 0
        assert(pos >= 0 || pos <= this->length);
        for (int i = pos; i < this->length - 2; i++) {
            this->elem[i] = this->elem[i + 1];
        }
        this->length -= 1;
    }

    void push_back(ElemType ele) {
        this->insert(ele, this->length);
    }

    ElemType pop_back() {
        this->erase(this->length - 1);
        return this->elem[this->length];
    }

    bool exist(ElemType aim) {
        for (int i = 0; i < this->length; i++) {
            if (this->elem[i] == aim) return true;
        }
        return false;
    }
};

// test
#include <iostream>

using namespace std;

int main() {
    while (!cin.eof()) {
        ArrayList<int> la, lb;

        //la get input
        int len, tmp;
        cin >> len;
        while (len--) {
            cin >> tmp;
            la.push_back(tmp);
        }

        //lb get input
        cin >> len;
        while (len--) {
            cin >> tmp;
            lb.push_back(tmp);
        }

        //output first two line
        for (int i = 0; i < la.length; i++) {
            if (i) cout << " ";
            cout << la.elem[i];
        }
        cout << endl;
        for (int i = 0; i < lb.length; i++) {
            if (i) cout << " ";
            cout << lb.elem[i];
        }
        cout << endl;

        for (int i = 0; i < lb.length; i++) {
            tmp = lb.elem[i];
            if (!la.exist(tmp)) {
                la.push_back(tmp);
            }
            // show la.list
            for (int j = 0; j < la.length; j++) {
                if (j) cout << " ";
                cout << la.elem[j];
            }
            cout << endl;
        }
        if(!cin.eof()) cout<<endl;
    }
    return 0;
}