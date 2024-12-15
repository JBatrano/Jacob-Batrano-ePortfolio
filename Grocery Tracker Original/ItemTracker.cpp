// ItemTracker.cpp

// Jacob Batrano
// Friday, Aug 11, 2023
// CS-210

#include "ItemTracker.h"

// Constructor: Initializes the frequency map by reading the input file.
ItemTracker::ItemTracker(const string &inputFileName, const string &outputFileName) {
    ifstream inputFile(inputFileName); // Opens the given input file for reading.
    ofstream outputFile(outputFileName); // Opens the given output file for writing.

    string item;
    // Reads each line from the input file and updates the frequency map.
    while (getline(inputFile, item)) {
        itemFrequency[item]++;
    }

    // Writes the item frequencies to the output file for backup.
    for (const auto &pair : itemFrequency) {
        outputFile << pair.first << " " << pair.second << endl;
    }

    // Closes the input and output files after use.
    inputFile.close();
    outputFile.close();
}

// Returns the frequency of the specified item.
int ItemTracker::getItemFrequency(const string &item) {
    // Checks if the item exists in the map.
    if (itemFrequency.find(item) != itemFrequency.end()) {
        return itemFrequency[item];
    }
    return 0; // If the item doesn't exist, returns 0.
}

// Displays all items along with their frequencies.
void ItemTracker::displayAllFrequencies() {
    for (const auto &pair : itemFrequency) {
        cout << pair.first << " " << pair.second << endl;
    }
}

// Displays a histogram of the item frequencies.
void ItemTracker::displayHistogram() {
    for (const auto &pair : itemFrequency) {
        cout << pair.first << " ";
        for (int i = 0; i < pair.second; i++) {
            cout << "*";
        }
        cout << endl;
    }
}
