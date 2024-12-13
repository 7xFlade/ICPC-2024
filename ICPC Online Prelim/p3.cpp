#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int s1, f1, h1, s2, f2, h2, s3, f3, h3;
    cin >> s1 >> f1 >> h1 >> s2 >> f2 >> h2 >> s3 >> f3 >> h3;
    int totalS = s1 + s2 + s3;
    int totalF = f1 + f2 + f3;
    int totalH = h1 + h2 + h3;
    int ans = totalS + totalF + totalH;
    string ansStr = "";

    if (totalF - f1 + totalH - h2 + totalS - s3 < ans) {
      ans = totalF - f1 + totalH - h2 + totalS - s3;
      ansStr = "FHS";
    }
    if (totalF - f1 + totalS - s2 + totalH - h3 < ans) {
      ans = totalF - f1 + totalS - s2 + totalH - h3;
      ansStr = "FSH";
    }
    if (totalH - h1 + totalF - f2 + totalS - s3 < ans) {
      ans = totalH - h1 + totalF - f2 + totalS - s3;
      ansStr = "HFS";
    }
    if (totalH - h1 + totalS - s2 + totalF - f3 < ans) {
      ans = totalH - h1 + totalS - s2 + totalF - f3;
      ansStr = "HSF";
    }
    if (totalS - s1 + totalF - f2 + totalH - h3 < ans) {
      ans = totalS - s1 + totalF - f2 + totalH - h3;
      ansStr = "SFH";
    }
    if (totalS - s1 + totalH - h2 + totalF - f3 < ans) {
      ans = totalS - s1 + totalH - h2 + totalF - f3;
      ansStr = "SHF";
    }

    cout << ansStr << " " << ans << endl;
  }
}