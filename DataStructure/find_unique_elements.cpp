#include <iostream>
using namespace std;

int main()
{
    int n, counter = 0, sum = 0;

    cout << "Enter array length: ";
    cin >> n;

    int arr[n], unique[n];

    cout << "Input the array: ";
    for (int i = 0; i < n; i++)
    {
        bool isExists = false;
        cin >> arr[i];
        for (int j = 0; j < counter; j++)
        {
            if (unique[j] == arr[i])
            {
                isExists = true;
                break;
            }
        }
        if (!isExists)
        {
            unique[counter] = arr[i];
            counter++;
        }
    }
    cout << "The unique elements are : [";
    for (int i = 0; i < counter; i++)
    {
        cout << unique[i] << " ";
        sum += unique[i];
    }
    cout << "]";
    cout << "The sum of the unique elements is: " << sum << endl;

    return 0;
}