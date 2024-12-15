import os

class ItemTracker:
    def __init__(self, input_file, output_file):
        """Initializes the frequency dictionary by reading the input file."""
        self.item_frequency = {}
        self.input_file = input_file
        self.output_file = output_file

        # Read items from the input file and populate item frequency dictionary
        try:
            with open(self.input_file, 'r') as file:
                for line in file:
                    item = line.strip()
                    if item:
                        self.item_frequency[item] = self.item_frequency.get(item, 0) + 1
            # Backup frequency data to output file
            self._backup_frequencies()
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' was not found.")

    def _backup_frequencies(self):
        """Writes item frequencies to an output file for backup."""
        try:
            with open(self.output_file, 'w') as file:
                for item, frequency in self.item_frequency.items():
                    file.write(f"{item} {frequency}\n")
        except IOError:
            print(f"Error: Could not write to the file '{self.output_file}'.")

    def get_item_frequency(self, item):
        """Returns the frequency of the specified item, case-insensitive."""
        item = item.lower()
        for key, frequency in self.item_frequency.items():
            if key.lower() == item:
                return frequency
        return 0

    def display_all_frequencies(self):
        """Displays all items along with their frequencies."""
        for item, frequency in self.item_frequency.items():
            print(f"{item}: {frequency}")

    def display_histogram(self):
        """Displays a histogram of the item frequencies."""
        for item, frequency in self.item_frequency.items():
            print(f"{item}: {'*' * frequency}")
