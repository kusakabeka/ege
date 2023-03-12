
#include <iostream>
#include <vector>

std::vector<unsigned> dividers(unsigned n)
{
    if (n == 0)
        return std::vector<unsigned>();

    std::vector<unsigned> divs(1, n);

    if (n == 1)
        return divs;

    for (unsigned d = n / 2; d > 1; --d)
        if (n % d == 0)
            divs.push_back(d);

    divs.push_back(1);

    return divs;
}

int main()
{
    unsigned n;

    std::cout << "Enter number: ";
    std::cin >> n;

    std::vector<unsigned> divs = dividers(n);

    if (divs.empty())
    {
        std::cout << "You enter 0" << std::endl;
    }
    else if (divs.size() == 2)
    {
        std::cout << "Number is prime" << std::endl;
    }
    else
    {
        std::cout << "Dividers: ";

        for (size_t i = 0; i < divs.size(); ++i)
            std::cout << divs[i] << "; ";

        std::cout << std::endl;
    }

    return 0;
}
