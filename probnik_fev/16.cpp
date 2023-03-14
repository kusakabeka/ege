#include <iostream>

long long funcc(int n) 
{
	if (n == 1)
	{
		return 1;
	} else {
		return n * funcc(n - 1);
	}
}

int main() {
	std::cout << funcc(1000) << '\n';

	return 0;
}