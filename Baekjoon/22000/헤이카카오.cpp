// 22353
#include <iostream>
#include <stdio.h>  

using namespace std;

int k, a;

double func(double d) {
    if(d >= 100) return a; // 무조건 이기므로 a만 필요
    double res = d * 0.01 * a + (100-d) * 0.01 * (func((1 + k * 0.01) * d) + a);
    return res;   
}

// 이길확률xA + 질확률x(증가된 담번에 이길 확률값 + a)

int main() {

    int d;
    cin >> a >> d >> k;

    double res = func(d);
    printf("%.7f\n", res);
}
