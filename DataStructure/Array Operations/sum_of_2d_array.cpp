#include <iostream>
using namespace std;

int main()
{
    int m, n, res = 0;
    cout << "Enter Row:" << endl;
    cin >> m;
    cout << "Enter Column:" << endl;
    cin >> n;
    int arr[m][n];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            cout << "Enter r" << i + 1 << "c" << j + 1 << ":";
            cin >> arr[i][j];
            res += arr[i][j];
        }
    cout << "Sum of the matrix: " << res;
}
