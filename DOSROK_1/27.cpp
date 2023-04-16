#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
    int n, k, m = 0;
    ifstream f("27A.txt");
    if (!f.is_open()) {
      cout << "Ошибка открытия файла" << endl;
    return 1;
    }
    f >> n;
    f >> k;
    vector<int>arr(n);
    for(int i = 0; i < n; ++i) f >> arr[i];
    for(int i = 0; i < n; ++i) {
      for(int j = i + 1; j < n; ++j){
          if((arr[i] + arr[j]) >= k) {
            m = max(m, arr[i] + arr[j]);
          }
        }
    }
    return 0;
}