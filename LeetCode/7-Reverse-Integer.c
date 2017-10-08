#ifndef CODEHUB_MAIN_H
#define CODEHUB_MAIN_H

#include <stdbool.h>

int reverse(int x) {
    int result = 0;
    while (x) {
        int temp = result * 10 + x % 10;
        if (temp / 10 != result) return 0;
        result = temp;
        x /= 10;
    }
    return result;
}

#endif //CODEHUB_MAIN_H
