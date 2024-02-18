# Builder Pattern
class Guest:
    def __init__(self):
        self.name = None
        self.phone_number = None
        self.email_address = None
        self.special_requests = None
        self.party_size = None

    #eventually this will tie in with the booking system
    def checkAvailability(self):
        import random
        is_available = random.choice([True, False])
        return is_available


    def makeReservation(self, room_type, length_of_stay):
        # eventually will make this logic to tie in with booking system
        print(f"Make reservation for {self.name} for {length_of_stay} nights for {self.party_size} in a {room_type} room.")

    def __str__(self):
        return f"Guest(name={self.name}, phone_number={self.phone_number}, email_address={self.email_address}, special_requests={self.special_requests}, party_size={self.party_size})"


class GuestBuilder:
    def __init__(self):
        self.guest = Guest()

    def set_name(self, name):
        self.guest.name = name
        return self

    def set_phone_number(self, phone_number):
        self.guest.phone_number = phone_number
        return self

    def set_email_address(self, email_address):
        self.guest.email_address = email_address
        return self

    def set_special_requests(self, special_requests):
        self.guest.special_requests = special_requests
        return self

    def set_party_size(self, party_size):
        self.guest.party_size = party_size
        return self

    def build(self):
        return self.guest



guest = GuestBuilder() \
    .set_name("Aaron Black") \
    .set_phone_number("123-456-7890") \
    .set_email_address("ablack5@live.maryville.edu") \
    .set_special_requests("None") \
    .set_party_size(4) \
    .build()

print(guest)

#automatically make reservation for testing purposes
availability = guest.checkAvailability()
if availability:
    guest.makeReservation("Double", 3)
else:
    print("Not available, try other dates")
