# Factory Design Pattern
class BookingSystemFactory:
    @staticmethod
    def create_booking( length_of_stay, room_type, guest):#eventually 'guest' will be the info from the guest class: guest = Guest
        if guest >= 1:
            return BookingSystem(length_of_stay, room_type, guest)
        else:
            raise ValueError("Invalid booking info")

class BookingSystem:
    def __init__(self, length_of_stay, room_type, guest):
        self.length_of_stay = length_of_stay
        self.room_type = room_type
        self.guest = guest

    # For now just to randomly display availability
    def display_availability(self):
        import random
        is_available = random.choice([True, False])  
        
        if is_available:
            self.book_room()
        else:
            print("Sorry, your room choice is unavailable")      
    
    def book_room(self):
        confirmation = input(f"We have abailability for room type '{self.room_type}' for {self.length_of_stay} nights with {self.guest} guest(s), would you like to confirm reservation (y/n)? ")   
        if confirmation.lower() == "y":
            self.process_reservation()  
        elif confirmation.lower() == "n":
            print("Thank you, please come book with us again soon!")
        else:
            print("Invalid input, please try booking again.")
    
    def process_reservation(self):       
        cost = self.length_of_stay * self.room_cost()
        self.send_confirmation(cost)
        print("Your room is booked, the confirmation has just been sent. Thank you for booking with us!")

    def send_confirmation(self,cost):
        guest_info = {self.guest, self.length_of_stay, self.room_type, cost}
        print(f"Your stay is confirmed for: \n{self.length_of_stay} nights \n-Guest Info-\nGuests: {self.guest} \nRoom Type: {self.room_type} \nCost: ${cost}" )
        return guest_info
    
    def room_cost(self):
        room_costs = {
            "Single": 100,
            "Double": 200,
            "Suite": 300
        }
        return room_costs.get(self.room_type, None) 

booking_system = BookingSystemFactory.create_booking(7, "Double", 2)
booking_system.display_availability()
booking_system = BookingSystemFactory.create_booking(5, "Single", 1)
booking_system.display_availability()
booking_system = BookingSystemFactory.create_booking(12, "Suite", 5)
booking_system.display_availability()