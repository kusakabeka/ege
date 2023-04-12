#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

std::vector<int> find_divs(int n)
{
    std::vector<int> divisiors;
    for (int i = 2; i < static_cast<int>(pow(n, 0.5)); ++i)
    {
        if (n % i == 0)
        {
            divisiors.push_back(i);
            if (i != n / i)
            {
                divisiors.push_back(n / i);
            }
        }
    }
    std::stable_sort(divisiors.begin(), divisiors.end());
    return divisiors;
}

int main()
{

    for (int n = 4000000; n < 12000000; ++n)
    {
        if (find_divs(n).size() == 5)
        {
            printf("%d %d", n, find_divs(n)[-1]);
        }
    }
    
    return 0;
}
