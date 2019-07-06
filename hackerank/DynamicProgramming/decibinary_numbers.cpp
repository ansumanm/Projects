#include <bits/stdc++.h>

using namespace std;

// Complete the decibinaryNumbers function below.

long get_decibinary(long deci) {
    string strnum = to_string(deci);
    long decibin = 0;
    int str_len = strnum.length();
    int i = 0;
    int tmp;

    for(auto it = strnum.rbegin(); it != strnum.rend(); ++it) {
        tmp = *it - '0';
        cout << tmp << endl;
        decibin +=  tmp * (1 << i);
        i++;
        cout << i << endl;
        cout << decibin << endl;
        cout << "##########" << endl;
    }

    return decibin;   
}

long decibinaryNumbers(long x) {
    long decinumber = x - 1;

    return get_decibinary(decinumber);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        long x;
        cin >> x;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        long result = decibinaryNumbers(x);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

