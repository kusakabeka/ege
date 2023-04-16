#include <iostream>
#include <vector>
using namespace std;

vector<int> divs(int n)
{
    vector<int> d;
    for (int i = 2; i < n / +1; ++i)
    {
        if (n % i == 0)
        {
            d.push_back(i);
        }
    }

    return d;
}

int main()
{
    for (int n = 50_000_000, n < 60_000_000; ++n)
    {
    }
    return 0;
}