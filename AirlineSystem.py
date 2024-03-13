class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

class Seat:
    def __init__(self, seat_number, seat_class):
        self.seat_number = seat_number
        self.seat_class = seat_class
        self.passenger = None

class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []
        self.waitlist = []
        self.seats = []

    def add_seat(self, seat_number, seat_class):
        self.seats.append(Seat(seat_number, seat_class))

    def book_seat(self, passenger, seat_number):
        if len(self.passengers) < self.capacity:
            for seat in self.seats:
                if seat.seat_number == seat_number and seat.passenger is None:
                    seat.passenger = passenger
                    self.passengers.append(passenger)
                    print(f"{passenger.name} booked seat {seat_number} on flight {self.flight_number}")
                    return True
            print(f"Seat {seat_number} is not available on flight {self.flight_number}")
        else:
            print(f"No available seats on flight {self.flight_number}")
        return False

    def cancel_booking(self, passenger):
        for seat in self.seats:
            if seat.passenger == passenger:
                seat.passenger = None
                self.passengers.remove(passenger)
                print(f"{passenger.name}'s booking canceled on flight {self.flight_number}")
                return True
        print(f"{passenger.name} does not have a booking on flight {self.flight_number}")
        return False

    def add_to_waitlist(self, passenger):
        if len(self.passengers) >= self.capacity:
            self.waitlist.append(passenger)
            print(f"{passenger.name} added to waitlist for flight {self.flight_number}")

class AirlineReservationSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def book_flight(self, flight_number, passenger, seat_number):
        if flight_number in self.flights:
            self.flights[flight_number].book_seat(passenger, seat_number)
        else:
            print(f"Flight {flight_number} not found")

    def cancel_booking(self, flight_number, passenger):
        if flight_number in self.flights:
            return self.flights[flight_number].cancel_booking(passenger)
        else:
            print(f"Flight {flight_number} not found")
            return False

    def add_to_waitlist(self, flight_number, passenger):
        if flight_number in self.flights:
            self.flights[flight_number].add_to_waitlist(passenger)
        else:
            print(f"Flight {flight_number} not found")

# Example usage:
if __name__ == "__main__":
    airline_system = AirlineReservationSystem()

    flight1 = Flight("AA123", "New York", "London", 200)
    flight1.add_seat("1A", "First Class")
    flight1.add_seat("1B", "First Class")
    flight1.add_seat("2A", "Business Class")
    flight1.add_seat("2B", "Business Class")
    flight1.add_seat("3A", "Economy Class")
    flight1.add_seat("3B", "Economy Class")

    airline_system.add_flight(flight1)

    passenger1 = Passenger("Alice", "ABC123")
    passenger2 = Passenger("Bob", "DEF456")
    passenger3 = Passenger("Charlie", "GHI789")

    airline_system.book_flight("AA123", passenger1, "1A")
    airline_system.book_flight("AA123", passenger2, "2A")
    airline_system.book_flight("AA123", passenger3, "3A")
    airline_system.book_flight("AA123", Passenger("David", "JKL012"), "1B")  # Attempt to book a full flight

    airline_system.cancel_booking("AA123", passenger2)

    airline_system.add_to_waitlist("AA123", Passenger("Eve", "MNO345"))  # Add passenger to waitlist
