#include <iostream>
#include <fstream>
#include <vector>
#include <time.h>
#include <climits> // для того, чтобы LLONG_MAX завелся
#include <cmath>
#include <algorithm>
#include <stdio.h>

using namespace std;
/*
    Настройки оптимизаци для Code::Blocks ->
    -Ofast
    -march=native
*/
int main(){int n;ifstream f("27b.txt");f >> n;vector<long long> a(n);for (int i = 0; i < n; ++i){f >> a[i]}; long long mx = LLONG_MAX, p, s, number = 0; for (int i = 0; i < n; ++i) { for (int j = i + 1; j < n; ++j{ p = 0; for (int j = i; j < n; ++j) { s = min(abs(i - j), n - abs(i - j)); p += s * a[j]; }if (p < mx) { mx = p; number = i + 1; } } if (i == 10000) cout << i << ' ' << clock() / 60000. * n / 10000 << '\n'; }cout << mx << '\n';return 0;}
