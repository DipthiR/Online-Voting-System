import json
import os
import getpass

USERS_FILE = "users.json"
CANDIDATES_FILE = "candidates.json"

class VotingSystem:
    def __init__(self):
        self.users = self.load_data(USERS_FILE, default={})
        self.candidates = self.load_data(CANDIDATES_FILE, default={})

    def load_data(self, filename, default):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return default

    def save_data(self):
        with open(USERS_FILE, 'w') as f:
            json.dump(self.users, f)
        with open(CANDIDATES_FILE, 'w') as f:
            json.dump(self.candidates, f)

    def register_user(self):
        username = input("Enter new username: ")
        if username in self.users:
            print("User already exists.")
            return
        password = getpass.getpass("Enter password: ")
        self.users[username] = {"password": password, "voted": False}
        self.save_data()
        print("User registered successfully!")

    def login_user(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        user = self.users.get(username)
        if user and user["password"] == password:
            if user["voted"]:
                print("You have already voted.")
                return None
            print("Login successful.")
            return username
        print("Invalid credentials.")
        return None

    def cast_vote(self, username):
        print("\nCandidates:")
        for i, candidate in enumerate(self.candidates, 1):
            print(f"{i}. {candidate}")
        try:
            choice = int(input("Select candidate number: ")) - 1
            selected = list(self.candidates.keys())[choice]
            self.candidates[selected] += 1
            self.users[username]["voted"] = True
            self.save_data()
            print(f"Vote cast successfully for {selected}!\n")
        except (IndexError, ValueError):
            print("Invalid selection. Vote not cast.")

    def view_results(self):
        print("\n--- Voting Results ---")
        for name, votes in self.candidates.items():
            print(f"{name}: {votes} vote(s)")
        print()

    def admin_panel(self):
        password = getpass.getpass("Enter admin password: ")
        if password != "admin123":
            print("Access denied.")
            return
        self.view_results()

    def main_menu(self):
        while True:
            print("\n--- Online Voting System ---")
            print("1. Register User")
            print("2. Login and Vote")
            print("3. View Results (Admin)")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.register_user()
            elif choice == '2':
                username = self.login_user()
                if username:
                    self.cast_vote(username)
            elif choice == '3':
                self.admin_panel()
            elif choice == '4':
                print("Exiting system...")
                break
            else:
                print("Invalid choice.")

def setup_default_data():
    if not os.path.exists(CANDIDATES_FILE):
        default_candidates = {"Alice": 0, "Bob": 0, "Charlie": 0}
        with open(CANDIDATES_FILE, 'w') as f:
            json.dump(default_candidates, f)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)

if __name__ == "__main__":
    setup_default_data()
    app = VotingSystem()
    app.main_menu()
