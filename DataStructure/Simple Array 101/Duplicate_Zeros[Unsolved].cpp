#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        bool start = false;
        int temp;
        for (int i = 0; i < arr.size(); i++)
        {
            if (start)
            {
                arr[i] = temp;
                if (i+1<arr.size())
                    temp = arr[i+1];
            }
            if (arr[i] == 0 && i+1<arr.size())
            {
                temp = arr[i+1];
                arr[i+1] = 0;
                start = true;
                i +=1;
            }
        }

    }
};
int main()
{
    Solution s;
    vector<int> n;
    int myints[] = {1,0,2,3,0,4,5,0};
    for (int i = 0; i < 8; i++)
    {
        n.push_back(myints[i]);
    }
    for (int i = 0; i < n.size(); i++)
    {
        cout << n[i] << endl;
    }
    
    s.duplicateZeros(n);

}