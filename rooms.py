from db import rooms


if rooms.count_documents({}) == 0: # it is to check whether the collection rooms is empty or not because every time main runs it will create duplicate rooms so it will insert rooms only if collection is empty


    rooms.insert_many([

        {"room_no":"101", "type":"single" , "price":1234 , "available":True},
        {"room_no":"102", "type":"double" , "price":2345 , "available":True},
        {"room_no":"103", "type":"triple" , "price":3456 , "available":True},

        {"room_no":"201", "type":"single" , "price":1456 , "available":True},
        {"room_no":"202", "type":"double" , "price":2654 , "available":True},
        {"room_no":"203", "type":"triple" , "price":3987 , "available":True},

        {"room_no":"301", "type":"single" , "price":1098 , "available":True},
        {"room_no":"302", "type":"double" , "price":2987 , "available":True},
        {"room_no":"303", "type":"triple" , "price":3789 , "available":True}

    ])

def view_rooms():
    all_rooms=rooms.find()

    for i in all_rooms:
        if((i["available"])==True):
            status="available"
        else:
            status="Not available"
        print("Room no.=",i["room_no"])
        print("type of room =",i["type"])
        print("Price=",i["price"])
        print(status,"\n")

def available_rooms():
    rooms_available=rooms.find({"available":True})
    for i in rooms_available:
        print("Room no :",i["room_no"])
        print("room type :",i["type"])
        print("Price :",i["price"],"\n")