from booking_template import Bookings
from db import bookings, rooms
from rooms import available_rooms, view_rooms


def create_booking():
    print("Rooms available :")
    available_rooms()

    id = input("Enter your customer id: ")
    choice = input("Enter the room no to be booked: ")

    confirm = input(f"Are you sure you want to book room no {choice} (Y/N): ")

    if confirm == 'Y':

        b1 = Bookings(id, choice)

        bookings.insert_one(b1.convert_to_dictionary())

        print("Booking confirmed")

        rooms.update_one(
            {"room_no": choice},
            {"$set": {"available": False}}
        )


def show_all_bookings():

    all_bookings = bookings.find()

    for i in all_bookings:

        print("Customer id:", i["customer_id"])
        print("Room no:", i["room_no"])
        print("-"*20)



def check_out():

    room_no = input("Enter the room no to be freed: ")

    bookings.delete_one({"room_no": room_no})

    rooms.update_one(
        {"room_no": room_no},
        {"$set": {"available": True}}
    )

    print("Checked out successfully")



def cancel_booking():

    room = input("Enter room number to cancel booking: ")

    bookings.delete_one({"room_no": room})

    rooms.update_one(
        {"room_no": room},
        {"$set": {"available": True}}
    )

    print("Booking cancelled")



def update_booking():

    id = input("Enter customer id: ")

    initial_room = input("Enter the current room number: ")

    new_room = input("Enter the new room no: ")


    bookings.update_one(

        {"customer_id": id},

        {"$set": {"room_no": new_room}}

    )


    rooms.update_one(

        {"room_no": new_room},

        {"$set": {"available": False}}

    )


    rooms.update_one(

        {"room_no": initial_room},

        {"$set": {"available": True}}

    )


    print("Booking updated successfully")