// main.cpp
#include "ItemTracker.h"

// Jacob Batrano
// Friday, Aug 11, 2023
// CS-210
#include "ItemTracker.h"

// Function to display the main menu and capture user's choice.
int displayMenu() {
    int choice;

    cout << "\n--- Corner Grocer Menu ---" << endl;
    cout << "1. Find frequency of a specific item." << endl;
    cout << "2. Display all item frequencies." << endl;
    cout << "3. Display frequency histogram." << endl;
    cout << "4. Exit." << endl;
    cout << "Enter your choice: ";
    cin >> choice;

    return choice;
}

int main() {
    const string inputFile = "/Users/rattlesnakejake/Desktop/Final cs-210/items.txt"; // File path for the items.
    ItemTracker tracker(inputFile, "frequency.dat"); // Initializes the ItemTracker object.

    int choice;
    do {
        choice = displayMenu(); // Displays the menu and gets user's choice.

        switch (choice) {
            case 1: {
                string item;
                cout << "Enter the name of the item: ";
                cin.ignore(); // Clears the input buffer.
                getline(cin, item); // Captures the entire item name from the user.

                cout << item << " appears " << tracker.getItemFrequency(item) << " times." << endl;
                break;
            }
            case 2:
                tracker.displayAllFrequencies(); // Displays all items and their frequencies.
                break;
            case 3:
                tracker.displayHistogram(); // Displays the histogram of item frequencies.
                break;
            case 4:
                cout << "Thank you for using the Corner Grocer program. Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice. Please choose a valid option." << endl;
        }
    } while (choice != 4);

    return 0;
}


