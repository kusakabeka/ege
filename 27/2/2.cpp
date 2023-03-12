#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
using namespace std;
/*
    Настройки оптимизаци для Code::Blocks ->
    -Ofast
    -march=native
*/


int main()
{
    int n;
    ifstream f("27b.txt");
    f >> n;
    vector<long long> a(n);
    for(int i = 0; i < n; ++i) f >> a[i];
    long long mx = 0;
    for(int i = 0; i < n; ++i)
    {
        for(int j = i + 1; j < n; ++j)
        {
            if ((a[i] + a[j]) % 2 == 0 && (a[i] % 23 == 0 || a[j] % 23 == 0)) mx = max(mx, a[i] + a[j]);
        }
        if (i == 10000) cout << i << ' ' << clock() << '\n';
    }
    cout << mx << '\n';
    return 0;
}
