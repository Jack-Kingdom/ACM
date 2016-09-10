#include <vector>
#include <iostream>

using namespace std;

int main() {
    do{
        vector<int> vec;
        int tmp;
        for (int i = 0; i < 10; i++) {
            cin >> tmp;
            vec.push_back(tmp);
        }

        tmp = vec[0];
        for (auto ele:vec) {
            if (ele > tmp) tmp = ele;
        }
        cout << "max=" << tmp << endl;
    }while(!cin.eof());
    return 0;
}