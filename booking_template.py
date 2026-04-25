class Bookings:
    def __init__(self,customer_id,room_no):
        self.customer_id=customer_id
        self.room_no=room_no
    
    def convert_to_dictionary(self):
        return {
            "customer_id":self.customer_id,
            "room_no":self.room_no
        }