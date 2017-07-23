#include <iostream>
#include <string>

using namespace std;


class Substitute {
public:
    int getValue(string key, string code) {
        int dict[100];
        for (int i = 0; i < 100; i++) dict[i] = -1;
        for (int i = 0; i < 10; i++) if (i == 9)dict[(int)key[i]] = 0; else dict[(int)key[i]] = i + 1;
        int result = 0;
        for (int i = 0; i < code.length(); i++) {
            int value = dict[(int)code[i]];
            if (value == -1) continue;
            else {
                result *= 10;
                result += value;
            }
        }
        return result;
    }
};

//int main() {
//    Substitute acm = Substitute();
//    int result = acm.getValue("TRADINGFEW", "LGXWEV");;
//    cout << result << endl;
//}