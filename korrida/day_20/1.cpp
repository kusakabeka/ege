#include <iostream>
#include <vector>

std::vector<int> divs(int n) {
    std::vector<int> d;
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            d.push_back(i);
        } 
    }
    return d;
}

int main() {
    for (int n = 416782; n < 498324; ++n) {
        std::vector<int> divisors = divs(n);
        int length = divisors.size();
        std::cout << "n: " << n << " --> divisors: ";
        if (length == 3) {  
            for (int j = 0; j < length; ++j) {
                std::cout << divisors[j] << " ";
            }   
        }
        std::cout << std::endl;
    }
    return 0;
}
