// ItemTracker.h

// Jacob Batrano
// Friday, Aug 11, 2023
// CS-210

#ifndef ITEMTRACKER_H
#define ITEMTRACKER_H

#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

class ItemTracker {
private:
    map<string, int> itemFrequency; // A map to store item frequencies.

public:
    // Constructor declaration.
    ItemTracker(const string &inputFileName, const string &outputFileName);
    
    // Method to get the frequency of a specific item.
    int getItemFrequency(const string &item);

    // Method to display all item frequencies.
    void displayAllFrequencies();

    // Method to display a frequency histogram.
    void displayHistogram();
};

#endif
