#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
/*
#define m = 80;
#define b = 50;
*/
int main()
{
    long long n;
    long long c = 0;
    ifstream f("27_B.txt");
    f >> n;
    vector<long long> a(n);
    for (long long i = 0; i < n; ++i) f >> a[i];
    for(long long i = 0; i < n; ++i)
    {
        for(long long j = i + 1; j < n; ++j)
        {
            if (((a[i] > 50) || (a[j] > 50)) && ((a[i] + a[j]) % 80 == 0))
            {
                c += 1;
            }
        }
    }
    cout << c << '\n';
    return 0;
}
