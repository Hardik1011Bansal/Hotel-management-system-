from customers import add_customer, view_customers, find, update, delete
from rooms import view_rooms, available_rooms
from bookings import create_booking, show_all_bookings, check_out, cancel_booking, update_booking


def customer_menu():

    while True:

        print("\n===== CUSTOMER MENU =====")

        print("1. Add customer")

        print("2. View customers")

        print("3. Find customer")

        print("4. Update customer")

        print("5. Delete customer")

        print("6. Back to main menu")


        choice = input("Enter choice: ")


        if choice == "1":

            add_customer()

        elif choice == "2":

            view_customers()

        elif choice == "3":

            find()

        elif choice == "4":

            update()

        elif choice == "5":

            delete()

        elif choice == "6":

            break

        else:

            print("Invalid choice")



def room_menu():

    while True:

        print("\n===== ROOM MENU =====")

        print("1. View all rooms")

        print("2. View available rooms")

        print("3. Back to main menu")


        choice = input("Enter choice: ")


        if choice == "1":

            view_rooms()

        elif choice == "2":

            available_rooms()

        elif choice == "3":

            break

        else:

            print("Invalid choice")



def booking_menu():

    while True:

        print("\n===== BOOKING MENU =====")

        print("1. Create booking")

        print("2. Show all bookings")

        print("3. Check-out")

        print("4. Cancel booking")

        print("5. Update booking")

        print("6. Back to main menu")


        choice = input("Enter choice: ")


        if choice == "1":

            create_booking()

        elif choice == "2":

            show_all_bookings()

        elif choice == "3":

            check_out()

        elif choice == "4":

            cancel_booking()

        elif choice == "5":

            update_booking()

        elif choice == "6":

            break

        else:

            print("Invalid choice")



def main():

    while True:

        print("\n========== HOTEL MANAGEMENT SYSTEM ==========")

        print("1. Customer operations")

        print("2. Room operations")

        print("3. Booking operations")

        print("4. Exit")


        choice = input("Enter your choice: ")


        if choice == "1":

            customer_menu()

        elif choice == "2":

            room_menu()

        elif choice == "3":

            booking_menu()

        elif choice == "4":

            print("Thank you for using the system")

            break

        else:

            print("Invalid choice")



if __name__ == "__main__":  #Every Python file has a special variable called: __name__  Python automatically sets its value depending on how the file is used.

    main()