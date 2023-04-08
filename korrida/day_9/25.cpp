#include <iostream>
#include <vector>

std::vector<int> divs_list(int number) {
    std::vector<int> arr;
    for (int i = 2; i <= number / 2; ++i) {
        if (number % i == 0) {
            arr.push_back(i);
        }
    }
    return arr;
}

int main() {
    for (int n = 4234679; n <= 10157812; ++n) {
        std::vector<int> divisors = divs_list(n);
        if (divisors.size() == 3) {
            std::cout << n << " " << divisors.back() << std::endl;
        }
    }
    return 0;
}
