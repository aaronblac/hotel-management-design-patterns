# Facade Pattern
class Reception:
    def __init__(self):
        self.employee_name = "" 
        self.guest_name = ""
        self.shift_time = ""
        self.checked_in_guests = set()#store checked in guest
    
    def checkInGuest(self, guest, employee, shift):
        if guest not in self.checked_in_guests:
            print(f"{guest} has been checked in by {employee} on the {shift} shift.")
            self.checked_in_guests.add(guest)
            print(self.checked_in_guests)
        else:
            print(f"{guest} is checked in already")
   
    def checkOutGuest(self, guest):
        if guest in self.checked_in_guests:
            print(f"{guest} has been checked out.")
            self.checked_in_guests.remove(guest)
            print(self.checked_in_guests)
        else:
            print(f"{guest} is not checked in.")
    
    #eventually will send this to housekeeping staff
    def handleSpecialRequest(self, request, guest):
        print(f"Special Request: {request} for {guest}")
    
    #will reintroduce when I can pull info from booking system
    # def takePayment(self, paymentAmount):
    #     pass
    
class ReceptionFacade:
    def __init__(self):
        self.reception = Reception()

    def check_in_guest(self, guest, employee, shift):
        return self.reception.checkInGuest(guest, employee, shift)

    def check_out_guest(self, guest):
        return self.reception.checkOutGuest(guest)

    def handle_special_request(self, request, guest):
        return self.reception.handleSpecialRequest(request, guest)

    # will reintroduce when I can pull info from booking system
    # def take_payment(self, payment_amount):
    #     return self.reception.takePayment(payment_amount)


reception_facade = ReceptionFacade()


reception_facade.check_in_guest("Aaron Black", "Jane", "Night")
reception_facade.check_in_guest("Dan Black", "Sally", "Day")
reception_facade.check_in_guest("Dan Black", "Sally", "Day")#check if else statement works
reception_facade.check_out_guest("Aaron Black")
reception_facade.check_out_guest("Aaron Black")#check if else statement works
reception_facade.handle_special_request("Bring extra towels", "Aaron Black")
