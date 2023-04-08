#include <iostream>
#include <fstream>
#include <vector>

int main() {

  int n;
  std::ifstream f("27A.txt");
  f >> n;
  std::vector<int> arr(n);
  for(int i = 0; i < n; ++i) f >> arr[i];
  for(int i = 0; i < n; ++i) {
    for(int j = i + 1; j < n; ++j) {
      
    }
  }
  
  
  
  return 0;
}