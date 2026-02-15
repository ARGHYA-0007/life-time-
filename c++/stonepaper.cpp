#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to convert shorthand to full word (for display)
string choiceToWord(char choice) 
{
    switch (choice) {
        case 's': return "Stone";
        case 'p': return "Paper";
        case 'x': return "Scissor";
        default: return "Invalid";
    }
}

// Function to get computer's choice
char getComputerChoice() 
{
    int random = rand() % 3;  // 0, 1, or 2
    if (random == 0) return 's';  // stone
    else if (random == 1) return 'p';  // paper
    else return 'x';  // scissor
}

// Function to decide winner
string getWinner(char user, char computer) 
{
    if (user == computer) return "Draw";

    if ((user == 's' && computer == 'x') ||
        (user == 'p' && computer == 's') ||
        (user == 'x' && computer == 'p')) 
        {
        return "You win!";
        }else 
    {
        return "Computer wins!";
    }
}

int main() 
{
    srand(time(0));  // Seed for randomness

    char userChoice;
    cout << "Enter your choice: (s = stone, p = paper, x = scissor): ";
    cin >> userChoice;

    // Validate input
    if (userChoice != 's' && userChoice != 'p' && userChoice != 'x') 
    {
        cout << "Invalid input. Please enter s, p, or x." << endl;
        return 1;
    }

    char computerChoice = getComputerChoice();
    cout << "You chose: " << choiceToWord(userChoice) << endl;
    cout << "Computer chose: " << choiceToWord(computerChoice) << endl;

    string result = getWinner(userChoice, computerChoice);
    cout << result << endl;

    return 0;
}
