// Code for Project2

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string filingStatus;
    double grossIncome;
    int dependents;
    
    cout << "What is your filing status? ";
    getline(cin, filingStatus);
    //cout << filingStatus;
    
    cout << "What is your adjusted gross income? ";
    cin >> grossIncome;
    
    cout << "How many children under the age of 17 did you claim as a dependent? ";
    cin >> dependents;
    
    if (filingStatus != "Single" && filingStatus != "Married" && filingStatus != "Head of Household")
        cout << "Error - Invalid filing status." << endl;
    else if (grossIncome < 0)
        cout << "Error - Invalid income." << endl;
    else if (dependents < 0)
        cout << "Error - Invalid number of dependents." << endl;
    else{
        int stimulus, maxIncome;
        if (filingStatus == "Married") {
            stimulus = 2400;
            maxIncome = 150000;
        } else {
            stimulus = 1200;
            if (filingStatus == "Single") {
                maxIncome = 75000;
            } else {
                maxIncome = 112500;
            }
        }
        stimulus += (dependents*500);

        if (grossIncome > maxIncome) {
            stimulus -= (((grossIncome - maxIncome)/100)*5);
        }

        cout << "Your stimulus check is $" << stimulus;


    }
        

    

}