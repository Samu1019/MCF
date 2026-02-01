#include <stdio.h>


double fib(int n) {
    if (n < 2) return 1.0;
    double prev = 1, curr = 1;
    for (int i = 3; i <= n; ++i) {
        double next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}
double fib_ratio(int n) {
    if (n < 2) return 1.0;
    double prev = 1, curr = 1;
    for (int i = 3; i <= n; ++i) {
        double next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr / prev;
}