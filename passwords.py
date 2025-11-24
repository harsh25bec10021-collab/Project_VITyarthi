import json
import os
import getpass


class PasswordManager:

    def __init__(self, data_file='passwords.json'):
        self.data_file = data_file
        self.data = {}
        self.load_data()

    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                print(f"Loaded {len(self.data)} entries from {self.data_file}")
            except Exception as e:
                print(f"Error loading data: {e}")
                self.data = {}
        else:
            self.data = {}
            print("No existing data file found. Starting fresh.")

    def save_data(self):
        """Save data to JSON file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_password(self, name, username, password):
        """Add a new password entry"""
        self.data[name.lower()] = {
            'name': name,
            'username': username,
            'password': password
        }
        self.save_data()
        print(f"Password for '{name}' added successfully!")

    def get_password(self, name):
        """Retrieve password by name"""
        name_lower = name.lower()
        if name_lower in self.data:
            entry = self.data[name_lower]
            return {
                'name': entry['name'],
                'username': entry['username'],
                'password': entry['password']
            }
        return None

    def get_all_passwords(self):
        """Get all stored passwords - useful for quick access"""
        return list(self.data.values())

    def search_passwords(self, search_term):
        """Search for passwords by name or username"""
        results = []
        search_lower = search_term.lower()

        for entry in self.data.values():
            if (search_lower in entry['name'].lower() or
                    search_lower in entry['username'].lower()):
                results.append(entry)

        return results

    def list_entries(self):
        """List all stored entries with full details"""
        if not self.data:
            print("No passwords stored.")
            return

        print(f"\n=== All Stored Passwords ({len(self.data)} entries) ===")
        print("=" * 60)

        for i, entry in enumerate(self.data.values(), 1):
            print(f"{i}. Name: {entry['name']}")
            print(f"   Username: {entry['username']}")
            print(f"   Password: {entry['password']}")
            print("-" * 60)

    def list_names_only(self):
        """List only names/services - quick overview"""
        if not self.data:
            print("No passwords stored.")
            return

        print(f"\n=== Stored Services ({len(self.data)} entries) ===")
        for i, entry in enumerate(self.data.values(), 1):
            print(f"{i}. {entry['name']} ({entry['username']})")

    def delete_entry(self, name):
        """Delete an entry by name"""
        name_lower = name.lower()
        if name_lower in self.data:
            deleted_entry = self.data[name_lower]
            del self.data[name_lower]
            self.save_data()
            print(f"Entry for '{deleted_entry['name']}' deleted successfully!")
            return True
        return False

    def export_to_file(self, filename):
        """Export all data to a readable text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Password Manager Export\n")
                f.write("=" * 50 + "\n\n")

                for i, entry in enumerate(self.data.values(), 1):
                    f.write(f"{i}. Service: {entry['name']}\n")
                    f.write(f"   Username: {entry['username']}\n")
                    f.write(f"   Password: {entry['password']}\n")
                    f.write("-" * 30 + "\n")

            print(f"Data exported to {filename}")
            return True
        except Exception as e:
            print(f"Export failed: {e}")
            return False

    def import_from_file(self, filename):
        """Import data from JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                imported_data = json.load(f)

            # Merge with existing data
            for key, value in imported_data.items():
                self.data[key] = value

            self.save_data()
            print(f"Successfully imported {len(imported_data)} entries from {filename}")
            return True
        except Exception as e:
            print(f"Import failed: {e}")
            return False


def main():
    pm = PasswordManager()

    print("=== Simple Password Manager ===")
    print("Note: Data is stored in plain text for easy access")

    while True:
        print("\n=== Menu ===")
        print("1. Add password")
        print("2. Get specific password")
        print("3. Show all passwords")
        print("4. Show names only")
        print("5. Search passwords")
        print("6. Delete entry")
        print("7. Export to text file")
        print("8. Import from JSON file")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == '1':
            name = input("Enter name/service: ").strip()
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if name and username and password:
                pm.add_password(name, username, password)
            else:
                print("All fields are required!")

        elif choice == '2':
            name = input("Enter name to search: ").strip()
            if name:
                entry = pm.get_password(name)
                if entry:
                    print(f"\nFound entry for '{entry['name']}':")
                    print(f"Username: {entry['username']}")
                    print(f"Password: {entry['password']}")
                else:
                    print(f"No entry found for '{name}'")
            else:
                print("Name is required!")

        elif choice == '3':
            pm.list_entries()

        elif choice == '4':
            pm.list_names_only()

        elif choice == '5':
            search_term = input("Enter search term: ").strip()
            if search_term:
                results = pm.search_passwords(search_term)
                if results:
                    print(f"\n=== Search Results for '{search_term}' ===")
                    for i, entry in enumerate(results, 1):
                        print(f"{i}. {entry['name']} - {entry['username']} - {entry['password']}")
                else:
                    print(f"No entries found for '{search_term}'")
            else:
                print("Search term is required!")

        elif choice == '6':
            name = input("Enter name to delete: ").strip()
            if name:
                if pm.delete_entry(name):
                    pass  # Success message already printed
                else:
                    print(f"No entry found for '{name}'")
            else:
                print("Name is required!")

        elif choice == '7':
            filename = input("Enter filename (default: passwords_export.txt): ").strip()
            if not filename:
                filename = "passwords_export.txt"
            pm.export_to_file(filename)

        elif choice == '8':
            filename = input("Enter JSON filename to import: ").strip()
            if filename and os.path.exists(filename):
                pm.import_from_file(filename)
            else:
                print("File not found or filename is required!")

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-9.")


def quick_access():
    """Quick function to get all passwords at once"""
    pm = PasswordManager()
    all_passwords = pm.get_all_passwords()

    if not all_passwords:
        print("No passwords stored.")
        return

    print("=== All Passwords (Quick Access) ===")
    for entry in all_passwords:
        print(f"{entry['name']}: {entry['username']} / {entry['password']}")


if __name__ == "__main__":
    # quick_access()

    main()