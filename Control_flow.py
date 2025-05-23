def switch_case(option):
    return {
        1: "You selected One",
        2: "You selected Two",
        3: "You selected Three"
    }.get(option, "Invalid choice")

while True:
    print("\nMenu:")
    print("1. Option One")
    print("2. Option Two")
    print("3. Option Three")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        print("Exiting program.")
        break

    print(switch_case(choice))
