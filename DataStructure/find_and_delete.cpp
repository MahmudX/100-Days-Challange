#include <iostream>
using namespace std;
int main()
{
    int sizeOfArray, temp, item, counter = 0;
    cout << "Enter Array size:\n";
    cin >> sizeOfArray;
    int arr[sizeOfArray + 1], i, j;
    cout << "\nEnter Array:\n";
    for (i = 0; i < sizeOfArray; i++)
    {
        cin >> arr[i];
    }
    cout << "\nEnter value of search :\n";

    cin >>        item;
    for (i = 0; i < sizeOfArray; i++)
    {
        if (arr[i] == item)
        {
            for (j = i; j < sizeOfArray - 1; j++)
            {
                arr[j] = arr[j + 1];
                counter++;
            }
        }
    }
    if (counter == 0)
    {
        cout << "\nItem isn't found.";
    }
    else
    {
        cout << "\nItem found and deleted successfully.\n";
        cout << "\nNew array is : ";
        for (j = 0; j < sizeOfArray - 1; j++)
        {
            cout << arr[j] << " ";
        }
    }
    cout << endl;
}