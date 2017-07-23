#include <iostream>

using namespace std;

struct subseq {
    int start = 0;
    int end = 0;
    int value = 0;
};

subseq function(int *sequence, int length) {
    subseq max = subseq(), last = subseq();
    max.value = INT32_MIN;    //important, numbers in sequence may be less than zero
    for (int i = 0; i < length; i++) {
        if (last.value >= 0) {
            last.value += sequence[i];
            last.end = i;
        }
        else {
            last.value = sequence[i];
            last.start = last.end = i;
        }
        if (max.value <= last.value) {
            max.value = last.value;
            max.start = last.start;
            max.end = last.end;
        }
    }
    return max;
}

int main() {
    int t, n;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        cin >> n;
        int *sequence = new int[n];
        for (auto i = 0; i < n; i++) {
            cin >> sequence[i];
        }
        subseq result = function(sequence, n);
        cout << "Case " << cs << ":" << endl << result.value << " " << result.start + 1 << " " << result.end + 1 <<
        endl;
        if (cs != t) cout << endl;
    }
    return 0;
}