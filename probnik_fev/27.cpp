#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	ifstream f("27B.txt");
	f >> n;
	vector<int> a(n);
	vector<int> b;
	for(int i = 0; i < n; ++i) f >> a[i];
	int mx = 0;
	for(int i = 0; i < n; ++i)
    {
        int k0 = 0, k1 = 0;
        for(int j = i; j < n; ++j)
        {
            if (a[j] % 2 == 0) {
                k0 += 1;
            } else {
                k1 += 1;
            }
            if (k1 == k0) {
                mx = max(mx, k0 + k1);
            }
        }
    }
    cout << mx << '\n';
	return 0;
}
