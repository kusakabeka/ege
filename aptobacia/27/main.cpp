#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() 
{
    int n;
    ifstream f("27A.txt");
    f >> n; // длина вектора
    vector<int> a(n);
    for (int i = 0; i < n; ++i) f >> a[i];


    return 0;
}
