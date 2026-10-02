buses = {
    1: {"name": "Hyderabad Express", "seats": 5},
    2: {"name": "Warangal Express", "seats": 5},
    3: {"name": "Vijayawada Express", "seats": 5}
}

bookings = []


def show_buses():
    print("\nAvailable Buses")
    print("-" * 40)

    for bus_id, bus in buses.items():
        print(
            f"{bus_id}. {bus['name']} - "
            f"{bus['seats']} seats available"
        )


def book_ticket():
    show_buses()

    try:
        bus_id = int(input("\nEnter bus number: "))

        if bus_id not in buses:
            print("Invalid bus number.")
            return

        if buses[bus_id]["seats"] == 0:
            print("No seats available.")
            return

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        bookings.append({
            "name": name,
            "age": age,
            "bus": buses[bus_id]["name"]
        })

        buses[bus_id]["seats"] -= 1

        print("\nTicket booked successfully!")


    except ValueError:
        print("Please enter valid details.")


def view_bookings():
    if not bookings:
        print("\nNo bookings found.")
        return

    print("\nBookings")
    print("-" * 40)

    for i, booking in enumerate(bookings, 1):
        print(f"{i}. Name: {booking['name']}")
        print(f"   Age: {booking['age']}")
        print(f"   Bus: {booking['bus']}")
        print()


def cancel_ticket():
    view_bookings()

    if not bookings:
        return

    try:
        number = int(input("Enter booking number to cancel: "))

        if number < 1 or number > len(bookings):
            print("Invalid booking number.")
            return

        cancelled = bookings.pop(number - 1)

        for bus_id, bus in buses.items():
            if bus["name"] == cancelled["bus"]:
                bus["seats"] += 1
                break

        print("Ticket cancelled successfully.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== BUS RESERVATION SYSTEM =====")
        print("1. Show Buses")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_buses()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
