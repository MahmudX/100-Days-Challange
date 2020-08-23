#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Enter N: ";
    cin >> n;
    int arr[n];
    string sb = "";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Original Array:\n"
         << sb << endl;
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ", ";
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (arr[j] < arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }

    cout << "After sorting in descending order:" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ", ";
    }
}