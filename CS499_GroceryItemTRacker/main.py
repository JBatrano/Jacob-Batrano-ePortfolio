from item_tracker import ItemTracker

def main_menu():
    """Displays the main menu and handles user choices."""
    tracker = ItemTracker(input_file="items.txt", output_file="frequency.dat")

    while True:
        print("\n--- Corner Grocer Menu ---")
        print("1. Find frequency of a specific item.")
        print("2. Display all item frequencies.")
        print("3. Display frequency histogram.")
        print("4. Exit.")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the name of the item: ").strip()
            frequency = tracker.get_item_frequency(item)
            print(f"{item} appears {frequency} time(s).")
        elif choice == '2':
            tracker.display_all_frequencies()
        elif choice == '3':
            tracker.display_histogram()
        elif choice == '4':
            print("Thank you for using the Corner Grocer program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu function to start the program
if __name__ == "__main__":
    main_menu()
