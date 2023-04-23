#include <iostream>
#include <vector>
#include <fstream>
#include <climits>

using namespace std;

int main()
{
    int n, c = 0;
    ifstream f("27-B.txt");
    f >> n;
    vector<long long> a(n);
    for(int i = 0; i < n; ++i) f >> a[i];
    for (int i = 0; i < n; ++i)
    {
        for(int j = i + 18; j < n; ++j)
        {
            if (((a[i] + a[j]) % 8 == 0) && ((a[i] * a[j]) % 2187 == 0))
                {
                    c += 1;
                }
        }
        if (i == 10000) cout << i << ' ' << clock()/60000. * n/10000 << '\n';

    }
    cout << c << '\n';
    return 0;
}
