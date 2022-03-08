# Create a class that captures airline tickets. Each ticket lists the departure and arrival cities,
# a flight number, and a seat assignment. A seat assignment has both a row and a letter for the seat
# within the row (such as 12F). Make two examples of tickets.

class Airlinetickets:
    i = 0

    def __init__(self, d, a, Fn, Sa):
        Airlinetickets.i += 1
        self.departure = d
        self.arrival = a
        self.flightnumber = Fn
        self.seatassignment = Sa

    def show(self):
        print("Tickets Deatil".center(50, "*"))
        print("Ticket", Airlinetickets.i)
        print("Departure City:", self.departure)
        print("Arrival City:", self.arrival)
        print("Flight Number:", self.flightnumber)
        print("Seat Assignment:", self.seatassignment)


a1 = Airlinetickets("Aurangabad", "Nanded", 12, "12F")
a1.show()
a1 = Airlinetickets("Nanded", "Pune", 13, "14P")
a1.show()
a1 = Airlinetickets("Nanded", "Pune", 13, "14P")
a1.show()