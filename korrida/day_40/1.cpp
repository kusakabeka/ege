#include <iostream>
#include <vector>
#include <fstream>

int main() {
    int n, min_odd_1, min_even_1, min_odd_2, min_even_2;
    std::ifstream f("1A.txt");
    f >> n;
    std::vector<int> arr(n);

    for(int i = 0; i < n; ++i) f >> arr[i];
}
