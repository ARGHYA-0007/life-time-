#include<iostream>
using namespace std;

int main() {
    float S, P, R, T;
    char c;

    cout << "Which variable do you want to calculate? (S/P/R/T): ";
    cin >> c;

    if(c == 'S') {
        cout << "Enter PRINCIPAL: ";
        cin >> P;
        cout << "Enter RATE (%): ";
        cin >> R;
        cout << "Enter TIME (years): ";
        cin >> T;
        cout << "Simple Interest = " << (P * R * T) / 100;
    }
    else if(c == 'P') {
        cout << "Enter SIMPLE INTEREST: ";
        cin >> S;
        cout << "Enter RATE (%): ";
        cin >> R;
        cout << "Enter TIME (years): ";
        cin >> T;
        cout << "Principal = " << (S * 100) / (R * T);
    }
    else if(c == 'R') {
        cout << "Enter SIMPLE INTEREST: ";
        cin >> S;
        cout << "Enter PRINCIPAL: ";
        cin >> P;
        cout << "Enter TIME (years): ";
        cin >> T;
        cout << "Rate = " << (S * 100) / (P * T);
    }
    else if(c == 'T') {
        cout << "Enter SIMPLE INTEREST: ";
        cin >> S;
        cout << "Enter PRINCIPAL: ";
        cin >> P;
        cout << "Enter RATE (%): ";
        cin >> R;
        cout << "Time = " << (S * 100) / (P * R);
    }
    else {
        cout << "Invalid input.";
    }

    return 0;
}
