#include <iostream>
using namespace std;
int main()
{
    int n, start, end, mid, item, position;
    cout << "Enter The size of your array : ";
    cin >> n;

    int arr[n];

    cout << "Enter a shorted array : ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Enter search item: ";
    cin >> item;

    start = 0;
    end = n - 1;
    mid = int(start + end) / 2;

    while (start <= end && arr[mid] != item)
    {
        if (item > arr[mid])
            start = mid + 1;
        else
            end = mid - 1;
        mid = (start + end) / 2;
    }

    if (arr[mid] == item)
        cout << "Item found at  Array index  no " << mid << endl;
    else
    {
        if (item > arr[mid])
            mid += 1;
        else if (mid > 0 && arr[mid] > item)
            mid -= 1;
        position = mid;

        for (int i = n - 1; i >= position; i--)
            arr[i + 1] = arr[i];

        arr[position] = item;
        n = n + 1;
        cout << "Item wasn't found. New item was inserted successfully." << endl;
        cout << "After adding the element new Array is: ";
        for (int i = 0; i < n; i++)
            cout << " " << arr[i];
    }
}