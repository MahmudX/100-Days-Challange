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
    int trans[n][m];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            cout << "Enter r" << i + 1 << "c" << j + 1 << ": ";
            cin >> arr[i][j];
            trans[j][i] = arr[i][j];
        }
    cout << "Matrix: " << endl;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
            cout << " " << arr[i][j] << " ";
        cout << endl;
    }

    cout << "Transpose Matrix:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cout << " " << trans[i][j] << " ";
        cout << endl;
    }
}
