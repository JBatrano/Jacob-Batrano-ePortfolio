from item_tracker import ItemTracker


def main_menu():
    """Displays the main menu and handles user choices."""
    tracker = ItemTracker(input_file="items.txt", output_file="frequency.dat")

    while True:
        print("\n" + "=" * 30)
        print("      Corner Grocer Menu")
        print("=" * 30)
        print("1. Find frequency of a specific item.")
        print("2. Display all item frequencies.")
        print("3. Display frequency histogram.")
        print("4. Add items to the database.")
        print("5. Delete an item.")
        print("6. Subtract item quantity.")
        print("7. Export data to CSV (optional).")
        print("8. Exit.")
        print("=" * 30)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the name of the item: ").strip()
            frequency = tracker.get_item_frequency(item)
            print(f"{item} appears {frequency} time(s).")
        elif choice == '2':
            print("\nAll Item Frequencies:")
            print("-" * 30)
            tracker.display_all_frequencies()
        elif choice == '3':
            print("\nItem Frequency Histogram:")
            print("-" * 30)
            tracker.display_histogram()
        elif choice == '4':
            item = input("Enter the name of the item: ").strip()
            if not item[0].isupper():
                print("Error: Item names must start with a capital letter.")
                continue
            try:
                quantity = int(input(f"Enter the quantity to add for '{item}': ").strip())
                tracker.add_item_to_database(item, quantity)
            except ValueError:
                print("Invalid input. Quantity must be a number.")
        elif choice == '5':
            item = input("Enter the name of the item to delete: ").strip()
            tracker.delete_item_from_database(item)
        elif choice == '6':
            item = input("Enter the name of the item: ").strip()
            try:
                quantity = int(input(f"Enter the quantity to subtract from '{item}': ").strip())
                tracker.subtract_item_quantity(item, quantity)
            except ValueError:
                print("Invalid input. Quantity must be a number.")
        elif choice == '7':
            filename = input("Enter the filename for export (or press Enter for 'grocery_data.csv'): ").strip()
            filename = filename if filename else "grocery_data.csv"
            tracker.export_to_csv(filename)
        elif choice == '8':
            print("Thank you for using the Corner Grocer program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




# Run the main menu function to start the program
if __name__ == "__main__":
    main_menu()
