#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() 
{
    int n;
    ifstream f("27A.txt");
    f >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i) f >> a[i];
    for(int i = 0; i < n; ++i) 
    {
        if (a[i] + a[i + 1] + a[i + 2])
    }
    return 0;
}

