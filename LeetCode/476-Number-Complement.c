int findComplement(int num) {
    int i=1;
    while(i<num) i= (i<<1) + 1;
    return i-num;
}
