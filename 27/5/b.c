#include <iostream>
#include <vector>
#include <fstream>
#include <climits>

using namespace std;

int main()
{
    int n, c = 0;
    ifstream f("27-B.txt");
    f >> n;
    vector<long long> a(n);
    vector<long long> b;
    for(int i = 0; i < n; ++i) f >> a[i];
    // sum % 8 == 0
    // proiz % 2187 == 0

    //Dividers: 2187; 729; 243; 81; 27; 9; 3; 1;
    for (int i = 0; i < n; ++i)
    {
        if a[i] % 2187 == 0 {b.push_back(a[i])}
        //Dividers: 2187; 729; 243; 81; 27; 9; 3; 1;
    }
    for(int i = 0; i < b.size(); ++i) {
        cout << b[i] << '\n';
    }
    return 0;
}
