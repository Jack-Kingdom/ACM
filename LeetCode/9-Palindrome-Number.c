#ifndef CODEHUB_MAIN_H
#define CODEHUB_MAIN_H

#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0 || (x != 0 && x % 10 == 0)) return false;

    int tmp = 0;
    while (x > tmp) {
        tmp = tmp * 10 + x % 10;
        x /= 10;
    }
    return x == tmp || x == tmp / 10;
}

#endif //CODEHUB_MAIN_H
