# user_comm.py
def display_menu() -> str:
    print("Menu")
    print("1. Load data")
    print("2. Show top categories")
    print("3. Show top channels by views")
    print("0. Exit")
    return input("Choose: ").strip()