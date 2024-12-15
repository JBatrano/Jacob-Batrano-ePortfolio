import os
import sqlite3  # Importing SQLite library for database handling


class ItemTracker:
    def __init__(self, input_file, output_file):
        """
        Initializes the ItemTracker object with the input file, output file,
        and sets up the SQLite database.
        """
        self.input_file = input_file  # Text file containing the item data
        self.output_file = output_file  # Backup file for item frequencies
        self.database = "grocery_items.db"  # SQLite database file name

        # Step 1: Initialize the database
        self._initialize_database()

        # Step 2: Populate the database with items from the input file
        self._populate_database()

        # Step 3: Debug database contents
        self._debug_display_database_contents()

    def _initialize_database(self):
        """
        Creates the SQLite database and the 'items' table if it doesn't exist.
        This table will store the item names and their frequencies.
        """
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    frequency INTEGER NOT NULL DEFAULT 0
                );
            ''')
            conn.commit()
            conn.close()
            print("Database initialized successfully.")
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def _populate_database(self):
        """
        Reads items from the input file and populates the database with their frequencies.
        If an item already exists in the database, its frequency is updated.
        """
        try:
            with open(self.input_file, 'r') as file:
                conn = sqlite3.connect(self.database)
                cursor = conn.cursor()

                for line in file:
                    item = line.strip().capitalize()  # Ensure items are capitalized
                    if item:
                        cursor.execute('''
                            INSERT INTO items (name, frequency)
                            VALUES (?, 1)
                            ON CONFLICT(name)
                            DO UPDATE SET frequency = frequency + 1;
                        ''', (item,))
                conn.commit()
                conn.close()
                print("Database populated with items from the input file.")
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' was not found.")
        except sqlite3.Error as e:
            print(f"Error populating database: {e}")

    def add_item_to_database(self, item, quantity):
        """
        Adds an item to the database. If the item exists, update its frequency.
        If the item does not exist, insert it with the specified quantity.
        """
        try:
            # Ensure the item starts with a capital letter
            if not item[0].isupper():
                print("Error: Item names must start with a capital letter.")
                return

            item = item.strip().capitalize()  # Capitalize the input
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO items (name, frequency)
                VALUES (?, ?)
                ON CONFLICT(name)
                DO UPDATE SET frequency = frequency + ?;
            ''', (item, quantity, quantity))
            conn.commit()

            cursor.execute('SELECT frequency FROM items WHERE name = ?', (item,))
            updated_frequency = cursor.fetchone()[0]
            conn.close()

            print(f"Added '{item}' to the database. Updated quantity: {updated_frequency}")
        except sqlite3.Error as e:
            print(f"Error adding item to the database: {e}")

    def subtract_item_quantity(self, item, quantity):
        """
        Subtracts a given quantity from an item's frequency in the database.
        Ensures the quantity does not go below zero.
        """
        try:
            item = item.strip().capitalize()  # Normalize item name
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            # Check if the item exists
            cursor.execute('SELECT frequency FROM items WHERE name = ?', (item,))
            result = cursor.fetchone()
            if result is None:
                print(f"Item '{item}' does not exist in the database.")
                conn.close()
                return

            # Calculate the new quantity
            current_quantity = result[0]
            new_quantity = max(0, current_quantity - quantity)

            # Update the database
            cursor.execute('UPDATE items SET frequency = ? WHERE name = ?', (new_quantity, item))
            conn.commit()
            conn.close()

            print(f"Updated '{item}' quantity. New quantity: {new_quantity}")
        except sqlite3.Error as e:
            print(f"Error updating item quantity: {e}")

    def delete_item_from_database(self, item):
        """
        Deletes an item from the database if it exists.
        """
        try:
            item = item.strip().capitalize()  # Normalize item name
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            # Check if the item exists
            cursor.execute('SELECT * FROM items WHERE name = ?', (item,))
            if cursor.fetchone() is None:
                print(f"Item '{item}' does not exist in the database.")
                conn.close()
                return

            # Delete the item
            cursor.execute('DELETE FROM items WHERE name = ?', (item,))
            conn.commit()
            conn.close()

            print(f"Item '{item}' has been deleted from the database.")
        except sqlite3.Error as e:
            print(f"Error deleting item from the database: {e}")

    def _debug_display_database_contents(self):
        """
        Debug method to display all items and their frequencies from the database.
        """
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute('SELECT name, frequency FROM items')
            rows = cursor.fetchall()
            conn.close()

            print("\n--- Debug: Current Database Contents ---")
            for row in rows:
                print(f"Item: {row[0]}, Frequency: {row[1]}")
            print("---------------------------------------")
        except sqlite3.Error as e:
            print(f"Error displaying database contents: {e}")

    def get_item_frequency(self, item):
        """
        Returns the frequency of a specified item (case-sensitive),
        fetched directly from the database.
        """
        try:
            item = item.strip().capitalize()  # Capitalize input for consistency
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            cursor.execute('SELECT frequency FROM items WHERE name = ?', (item,))
            result = cursor.fetchone()
            conn.close()

            if result:
                return result[0]
            else:
                print(f"DEBUG: Item '{item}' not found in the database.")
                return 0
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            return 0

    def display_all_frequencies(self):
        """
        Displays all items and their frequencies in a table format.
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT name, frequency FROM items ORDER BY name ASC')
            rows = cursor.fetchall()
            conn.close()

            print(f"{'Item':<15} {'Frequency':<10}")
            print("-" * 25)
            for row in rows:
                print(f"{row[0]:<15} {row[1]:<10}")
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            conn.close()

    def display_histogram(self):
        """
        Displays a histogram of item frequencies using '*' to represent counts.
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT name, frequency FROM items')
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                print(f"{row[0]}: {'*' * row[1]}")
        except sqlite3.Error as e:
            print(f"Error querying database: {e}")
            conn.close()

    def export_to_csv(self, filename="grocery_data.csv"):
        """
        Exports the items and their frequencies to a CSV file.
        """
        import csv

        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()

            # Fetch all items from the database
            cursor.execute('SELECT name, frequency FROM items')
            rows = cursor.fetchall()
            conn.close()

            # Write the data to a CSV file
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Item", "Frequency"])  # Write the header
                writer.writerows(rows)

            print(f"Data exported successfully to '{filename}'.")
        except sqlite3.Error as e:
            print(f"Error exporting data: {e}")
        except IOError as e:
            print(f"Error writing to file: {e}")


