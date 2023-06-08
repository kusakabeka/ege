#include <bits/stdc++.h>

int fib(int n) {
    int a = 0, b = 1, c, i;
    if (n == 0) 
        return a;
    for (int i = 0; i <= n; ++i)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;

}

int main(int argc, char const *argv[])
{
    
    int n = 7;

    std::cout << fib(n);
    return 0;
}