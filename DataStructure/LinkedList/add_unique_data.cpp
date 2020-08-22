#include<iostream>
using namespace std;
class LinkedList
{
private:
    struct node
    {
        int data[2];
        node* next;
    };
    typedef struct node* Node;
    Node head;
    Node current;
public:
    int UniqueLength;
    LinkedList()
    {
        head = NULL;
        current = NULL;
        UniqueLength = 0;
    }   
    void AddUniqueNode(int data)
    {
        Node n = new node;
        n->data[0] = data;
        n->data[1] = 1;
        n->next = NULL;
        if (head != NULL)
        {
            bool isExists = false;
            current = head;
            while (current->next != NULL)
            {
                // Checks if already exists
                if (current->data[0] == data)
                {
                    // if exists, increases the count 
                    // and breaks the while loop.
                    current->data[1] += 1;
                    isExists = true;
                    break;
                }
                current = current->next;
            }
            if (!isExists) {
                // Adds the item if not exists 
                // in the list already.
                current->next = n;
                UniqueLength += 1;
            }
            /*
            IF we remove line no (37-45),(48-50),(52,53)
            all the element gets added to the list and
            traversing prints all the element. but if we do
            not remove, something strange hapens.
            */
        }
        else
        {
            // Adds the first item to the list
            head = n;
            UniqueLength = 1;
        }
    }
    void PrintList()
    {
        current = head;
        while (current != NULL)
        {
            cout << current->data[0] << endl;
            current = current->next;
        }
    }
};

int main()
{   
    LinkedList ln;
    ln.AddUniqueNode(50);
    ln.AddUniqueNode(5);
    ln.AddUniqueNode(5);
    ln.AddUniqueNode(5);
    ln.AddUniqueNode(6);
    ln.AddUniqueNode(6);
    ln.AddUniqueNode(5);
    ln.PrintList();
    cout << "Total Length: " << ln.UniqueLength;
    /*
    Output:
            50
            5
            5
            6
            6
            Total Length: 5
    */
    /*
    Expected:
            50
            5
            6
            Total Length: 3
    */
}