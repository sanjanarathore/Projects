// Code for Project 3

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool isWellFormedGroceryOrderString(string grocerystring)
{
    for(int i = 0; i < grocerystring.length(); i++) 
    {
        grocerystring[i] = tolower(grocerystring[i]);
        char c = grocerystring[i];
        //if (!isdigit(grocerystring[i]) && !isalpha(grocerystring[i]))
            //return false;
        if (!isdigit(c))    // if not a digit and not an alphabet (unless its p, d, s) return false
        {
            if((c != 'p') && (c != 'd') && (c != 's') && (c != 'i'))
            {
                return false;
            }
        }
    }

    int pVal = 0, sVal = 0, dVal = 0, iVal = 0;
    for (int i = 0; i < grocerystring.length(); i++)
    {
        string substr = "";
        if (isalpha(grocerystring[i])) // if i is index of a letter find next previous letter
        {
            for(int j = i-1; j >= 0 && i-j <= 3; j--)
            {
                if (isalpha(grocerystring[j])) //
                {
                    substr = grocerystring.substr(j+1, i-j-1);
                    if (substr[0] == '0')
                        return false;
                    break;
                }   
                else if (j == 0) // to get number at beginning of string
                {
                     substr = grocerystring.substr(0, i-j);
                        if (substr[0] == '0') // || (isdigit(substr[0] && substr.length() == 3)))   // if start with a 0 or is a three digit number --> entire string invalid
                        return false;
                     break;
                }
                if (i-j == 3 && isdigit(grocerystring[j]))     // if its a 3 digit number --> entire string invalid
                    return false;
            }
            
            if (substr.length() > 0)
            {
                int num = stoi(substr);
                if (grocerystring[i] == 'p') 
                    pVal += num;
                else if (grocerystring[i] == 's')
                    sVal += num;
                else if (grocerystring[i] == 'd')
                    dVal += num;
                else if (grocerystring[i] == 'i')
                    iVal += num;
            }
            else            // two letters in a row invalid
                return false;

        } 
    }

    if (pVal > 20)
        return false;
    else if (dVal > 10)
        return false;
    else if (pVal + dVal + sVal + iVal > 99)
        return false;


    return true;
}


int pickupCount(string grocerystring)
{
    int pCount = 0;
    if(isWellFormedGroceryOrderString(grocerystring))
    {   
        for (int i = 0; i < grocerystring.length(); i++) 
        {
            if (grocerystring[i] == 'p')
            {
                pCount += grocerystring[i-1] - '0';
                if (isdigit(grocerystring[i-2]) && i-2 >= 0)
                    //cout << "2 dig";
                    pCount += 10*(grocerystring[i-2] -'0');
            }
        }
    }
    return pCount;
}



int main()
{
    string gs;
    cout.setf( ios::boolalpha );
    cout << "Enter string: ";
    cin >> gs;
    cout << isWellFormedGroceryOrderString(gs) << endl;
    cout << pickupCount(gs) << " pickups" << endl;
}