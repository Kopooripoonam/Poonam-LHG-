#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a ;
    long b;
    char ch;
    float d;
    double e;
    scanf("%d %ld %c %f %lf", &a, &b, &ch, &d, &e); //reads input for all
    printf("%d\n%ld\n%c\n%.3f\n%.9lf\n", a , b, ch, d, e);
    return 0;
}
