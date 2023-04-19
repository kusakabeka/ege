#include <iostream>
#include <vector>

int divs_count(int n) {
	int count = 0;
	for(int i = 2; i < (n / 2) + 1; ++i) {
		if (n % i == 0) {
			count += 1;
		}
	}
	return count;
} 

int main() {
	for(int n = 26600; n < 28100; ++n) {
		if ((divs_count(n) > 0) && (divs_count(n) % 13 == 0)) {
			std::cout << n << " " <<divs_count(n) << '\n';
		}
	}
	return 0;
}