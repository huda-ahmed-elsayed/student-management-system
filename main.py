from students import get_id, add_student, view_students, search_student, update_student, delete_student
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("\033[1;36m")
    print("╔══════════════════════════════════╗")
    print("║   🎓 Student Management System   ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Add Student                  ║")
    print("║  2. View Students                ║")
    print("║  3. Search for Student           ║")
    print("║  4. Update Student               ║")
    print("║  5. Delete Student               ║")
    print("║  6. Exit                         ║")
    print("╚══════════════════════════════════╝")
    print("\033[0m")

while True:
    clear()
    print_menu()
    
    choice = input("Enter your choice: ")

    if choice == "1":
        id = get_id()
        if id is None:
            input("\nPress Enter to continue...")
            continue
        name = input("Enter your Name: ")
        try:
            age = int(input("Enter your Age: "))
        except ValueError:
            print("\033[1;31mAge must be a number.\033[0m")
            input("\nPress Enter to continue...")
            continue
        track = input("Enter your Track: ")
        add_student(id, name, age, track)
        input("\nPress Enter to continue...")

    elif choice == "2":
        clear()
        view_students()
        input("\nPress Enter to continue...")

    elif choice == "3":
        id = get_id()
        if id is None:
            input("\nPress Enter to continue...")
            continue
        search_student(id)
        input("\nPress Enter to continue...")

    elif choice == "4":
        id = get_id()
        if id is None:
            input("\nPress Enter to continue...")
            continue
        update_student(id)
        input("\nPress Enter to continue...")

    elif choice == "5":
        id = get_id()
        if id is None:
            input("\nPress Enter to continue...")
            continue
        delete_student(id)
        input("\nPress Enter to continue...")

    elif choice == "6":
        clear()
        print("\033[1;32m👋 Goodbye!\033[0m\n")
        break

    else:
        print("\033[1;31mInvalid choice! Please choose a number between 1 and 6.\033[0m")
        input("\nPress Enter to continue...")