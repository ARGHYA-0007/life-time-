#include <iostream>
using namespace std;

int main() 
{
    int number, count = 0;

    cout << "Enter a number: ";
    cin >> number;

    // Prime numbers are greater than 1
    if (number <= 1) 
    {
        cout << number << " is not a prime number." << endl;
        return 0;
        
    }

    // Count how many numbers divide 'number'
    for (int i = 1; i <= number; i++) {
        if (number % i == 0) 
        {
            count++;
        }
    }

    // If number has only 2 divisors (1 and itself), it's prime
    if (count == 2)
        cout << number << " is a prime number." << endl;
    else
        cout << number << " is not a prime number." << endl;

    return 0;
}
