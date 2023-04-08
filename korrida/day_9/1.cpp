#include <iostream>
#include <vector>

int sum_min_max_divisors(int n) {
  std::vector<int> divisors;
  for (int i = 2; i * i <= n; ++i) {
    if (n % i == 0) {
      divisors.push_back(i);
      if (i != n / i) {
        divisors.push_back(n / i);
      }
    }
  }
  if (divisors.empty()) {
    return 0;
  } else {
    int min_divisor = *std::min_element(divisors.begin(), divisors.end());
    int max_divisor = *std::max_element(divisors.begin(), divisors.end());
    return min_divisor + max_divisor;
  }
}

int main() {
  int count = 0;
  for (int n = 452021; count < 5; ++n) {
    if (sum_min_max_divisors(n) % 7 == 3) {
      std::cout << n << " " << sum_min_max_divisors(n) << std::endl;
      ++count;
    }
  }
  return 0;
}
