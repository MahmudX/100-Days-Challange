#include <iostream>
using namespace std;
int main()
{
    int n, item, counter = 0;
    bool isFound = false;

    cout << "Enter Array size: ";
    cin >> n;
    int arr[n + 1];

    cout << "Enter Array: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter value of search : ";
    cin >> item;

    for (int i = 0; i < n; i++)
        if (arr[i] == item)
        {
            isFound = true;
            for (int j = i; j < n - 1; j++)
                arr[j] = arr[j + 1];
        }

    if (isFound)
    {
        cout << "Item found and deleted successfully." << endl;
        cout << "New array is : ";
        for (int i = 0; i < n - 1; i++)
            cout << arr[i] << " ";
    }
    else
        cout << "Item wasn't found." << endl;
}