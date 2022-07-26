// Program to verify input constraints

#include <bits/stdc++.h>

using namespace std;

// !! This is a sample !!
// Must be configured accordingly
int main() {
    const int MAX_T = 100;
    const int MAX_N = 1000;
    const int MAX_A = 1e9;
    ifstream inputs;
    inputs.open("inputs.txt");
    while(!inputs.eof()) {
        string input;
        inputs >> input;
        if(input == "") {
            continue;
        }
        cout << input << ": ";
        std::ifstream cin("./tests/inputs/" + input);
        short t;
        cin >> t;
        if(t <= 0 || t > MAX_T) {
            cout << "WA (Invalid t)" << "\n";
            return -1;
        }
        int tot = 0;
        while(t--) {
            int n;
            cin >> n;
            if(n < 2 || n > MAX_N) {
                cout << "WA (Invalid n)" << "\n";
                return -1;
            }
            tot += n;
            for(int i = 0; i < n; i++) {
                int a;
                cin >> a;
                if(a <= 0 || a > MAX_A) {
                    cout << "WA (Invalid a)" << "\n";
                    return -1;
                }
            }
        }
        if(tot > MAX_N) {
            cout << "WA (n over test cases is exceeding)" << "\n";
            return -1;
        }
        cout << "AC" << "\n";
    }
    inputs.close();
    return 0;
}
