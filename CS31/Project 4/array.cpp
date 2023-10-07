// Code for Project 4

#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int locateMinimum(const string array[ ], int n)
{
    if (n <= 0)
        return -1;
    else
    {
        int minIndex = 0;
        for (int i = 1; i < n; i++)
        {
            if (array[i] < array[minIndex])
                minIndex = i;
        }
        return minIndex;
    }
}

int countPunctuation(const string array[ ], int  n)
{
    if (n <= 0)
        return -1;
    else
    {
        int puncCount = 0;
        char punctuation[10] = {',', '.', ':', '-', '?', '!', ':', '"', '(', ')'};
        for (int i = 0; i < n; i++)
        {
            string str = array[i];
            for (int j = 0; j < str.size(); j++)
            {
                for (int k = 0; k < 10; k++) 
                {
                    if (str[j] == punctuation[k])
                        puncCount++;
                }
            }
        }
        return puncCount++;
    }
}


bool hasReverse(const string array[ ], int n)
{
    if (n <= 0)
        return false;
    else
    {
        for (int i = 0; i < n; i++)
        {
            string str = array[i];
            for (int j = 0; j < str.size()/2; j++)
            {
                char temp = str[j];
                str[j] = str[str.size()-1-j];
                str[str.size()-1-j] = temp;
            }
            for (int k = i+1; k < n; k++)
            {
                if (array[k] == str) 
                    return true;
            }
        }
        return false;
    }
}

char highestOccurredCharacter(const string array[ ], int n, int index)
{
    if (n <= 0 || index < 0 || index >= n)
        return '"';
    else
    {
        string str = array[index];
        int len = str.size();
        int letters[len];
        for (int i = 0; i < len; i++)
        {
            letters[i] = 1;
        }
        for (int i = 1; i < len; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (str[i] == str[j]) {
                    letters[i]++;
                }
            }
        }
        int maxIndex = 0;
        for (int i = 0; i < len; i++) 
        {
            if (letters[i] > letters[maxIndex]) 
                maxIndex = i;
        }
        return str[maxIndex];

    }

}

bool isInIncreasingOrder(const string array[ ], int  n)
{
    if (n <= 0)
        return false;
    else
    {
        for (int i = 0; i < n-1; i++) 
        {
            if (array[i] > array[i+1])
                return false;
        }
        return true;
    }
}

char firstNonRepeatedCharacter(const string array[ ], int n, int index)
{
    if (n <= 0 || index < 0 || index >= n)
        return '"';
    else 
    {
        string str = array[index];
        
        for (int i = 0; i < str.size(); i++) 
        {
            bool rep = false;
            for (int j = 0; j < str.size(); j++) 
            {
                if (i == j)
                    continue;
                else 
                {
                    if (str[i] == str[j])
                    {
                        rep = true;
                        break;
                    }
                }
            }
            if (rep == false) {
                return str[i];
            }
        }
        return '"';
    }
}

bool isOnlyDigits(const string array[ ], int n)
{
    if (n <= 0)
        return false;
    else 
    {
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < array[i].size(); j++) 
            {
                if (!isdigit(array[i][j]))
                    return false;
            }
        }
        return true;
    }
}

int main() 
{
    cout.setf( ios::boolalpha );
    string people[5] = { "jon", "mamabbcc!", "samwell,", "daenerys.", "tyrion"};
    string folks[8] = {"samwell", "jon", "margaery", "daenerys", "tyrion", "sansa", "llewmas", "noj"};
    string nums[3] = {"324", "34", "98s"};
    // cout << locateMinimum(people, 5) << endl;
    // cout << countPunctuation(people, 5) << endl;
    // cout << hasReverse(people, 5) << endl;
    // cout << hasReverse(folks, 8) << endl;
    cout << isInIncreasingOrder(people, 5) << endl;
    cout << isInIncreasingOrder(people, 3) << endl;
    cout << isOnlyDigits(nums, 3) << endl;
    cout << firstNonRepeatedCharacter(people, 5, 1) << endl;
    cout << highestOccurredCharacter(people, 5, 3);


    // string test = "abcde";
    // test[0] = 'b';
    // cout << test;
}